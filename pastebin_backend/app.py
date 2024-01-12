from flask import Flask, jsonify, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from dotenv import load_dotenv
import os

from logging import Logger

logger = Logger(__name__)

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pastebin.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

from models import User, Paste

@app.route('/')
@jwt_required()
def index():
    current_username = get_jwt_identity()  # Get the current user's username from the JWT token
    # First, get the user by username
    user = User.query.filter_by(username=current_username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Query the database for pastes created by the current user
    user_pastes = Paste.query.filter_by(user_id=user.id).order_by(Paste.created_at.desc()).all()

    # Convert the pastes to a suitable format for rendering
    pastes_data = [{'id': paste.id, 'content': paste.content, 'created_at': paste.created_at} for paste in user_pastes]

    # Render the home view with the user's pastes
    return render_template('index.html', pastes=pastes_data)


@app.route('/api/pastes', methods=['POST'])
@jwt_required(optional=True)
def create_paste():
    current_username = get_jwt_identity()  # Get the current user's username from the JWT token
    if current_username is not None:
        user = User.query.filter_by(username=current_username).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        user_id = user.id
    else:
        user_id = 'anonymous'
    content = request.json.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    paste = Paste(content=content, user_id=user_id)  # Use the user's ID for the paste
    db.session.add(paste)
    db.session.commit()

    return jsonify({'message': 'Paste created successfully', 'id': paste.id}), 201

@app.route('/api/pastes', methods=['GET'])
@jwt_required(optional=True)
def get_pastes():
    current_username = get_jwt_identity()
    if current_username is not None:
        # If the user is logged in, return only their pastes
        user = User.query.filter_by(username=current_username).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        user_pastes = Paste.query.filter_by(user_id=user.id).order_by(Paste.created_at.desc()).all()
    else:
        # For unauthenticated users, return empty list
        user_pastes = []

    return jsonify([{'id': paste.id, 'content': paste.content, 'created_at': paste.created_at} for paste in user_pastes])


@app.route('/api/pastes/<int:paste_id>', methods=['GET'])
def view_paste(paste_id):
    paste = Paste.query.get(paste_id)
    if not paste:
        return jsonify({'error': 'Paste not found'}), 404

    return jsonify({'id': paste.id, 'content': paste.content, 'created_at': paste.created_at})

@app.route('/api/pastes/search', methods=['GET'])
def search_pastes():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400

    pastes = Paste.query.filter(Paste.content.contains(keyword)).all()
    if not pastes:
        return jsonify({'error': 'No pastes found for the given keyword'}), 404

    return jsonify([{'id': paste.id, 'content': paste.content, 'created_at': paste.created_at} for paste in pastes])

@app.route('/api/pastes/<int:paste_id>', methods=['DELETE'])
@jwt_required()
def delete_paste(paste_id):
    try:
        paste = Paste.query.get(paste_id)
        if not paste:
            return jsonify({'error': 'Paste not found'}), 404
        current_user = get_jwt_identity()
        if paste.user_id != current_user:
            return jsonify({'error': 'You are not authorized to delete this paste'}), 401
        db.session.delete(paste)
        db.session.commit()
        return jsonify({'message': 'Paste deleted successfully'})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 422


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful. Please log in.', 'success')
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = create_access_token(identity=username)
        return jsonify(token=token), 200

    return jsonify({'error': 'Invalid username or password'}), 401


@app.route('/api/logout')
@jwt_required()
def logout():
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/api/username', methods=['GET'])
@jwt_required()
def get_username():
    current_username = get_jwt_identity()
    return jsonify(username=current_username), 200

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)