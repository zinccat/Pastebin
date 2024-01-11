from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from app import app, db, login_manager
from models import User, Paste

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pastes', methods=['POST'])
@login_required
def create_paste():
    content = request.json.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    paste = Paste(content=content, user_id=current_user.id)
    db.session.add(paste)
    db.session.commit()
    return jsonify({'message': 'Paste created successfully'}), 201

@app.route('/api/pastes', methods=['GET'])
def get_pastes():
    pastes = Paste.query.all()
    print(pastes)
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
@login_required
def delete_paste(paste_id):
    paste = Paste.query.get(paste_id)
    if not paste:
        return jsonify({'error': 'Paste not found'}), 404

    if paste.user_id != current_user.id:
        return jsonify({'error': 'You do not have permission to delete this paste'}), 403

    db.session.delete(paste)
    db.session.commit()
    return jsonify({'message': 'Paste deleted successfully'})

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful. Please log in.', 'success')
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/api/login', methods=['POST', 'GET'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401

    login_user(user)
    return jsonify({'message': 'Login successful'})

@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)