from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import random
# import uuid
# from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
    # Todo: do not allow username to be set as 'anonymous'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.id

class Paste(db.Model):
    id = db.Column(db.String(80), primary_key=True, default=lambda: generate_id())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with open('words.txt') as f:
    words = f.read().splitlines()
    
def generate_id():
    return '-'.join(random.sample(words, 4))