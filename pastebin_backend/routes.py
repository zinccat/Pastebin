from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from app import app, db, jwt
from models import User, Paste

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pastes', methods=['POST'])
@jwt_required()
def create_paste():
    try:
        content = request.json.get('content')
        if not content:
            return jsonify({'error': 'Content is required'}), 400

        paste = Paste(content=content, user_id=1) # TODO: Replace 1 with current_user.id
        db.session.add(paste)
        db.session.commit()
        return jsonify({'message': 'Paste created successfully'}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 422

@app.route('/api/pastes', methods=['GET'])
def get_pastes():
    pastes = Paste.query.all()
    # reverse=True to get the latest pastes first
    pastes = sorted(pastes, key=lambda paste: paste.created_at, reverse=True)
    return jsonify([{'id': paste.id, 'content': paste.content, 'created_at': paste.created_at} for paste in pastes])

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


if __name__ == '__main__':
    app.run(debug=True)