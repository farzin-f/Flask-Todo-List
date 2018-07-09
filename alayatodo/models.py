import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    todos = db.relationship('Todo', backref='user', lazy='select')

    # Return the string representation of the User model (debugging)
    def __repr__(self):
        return '<User %r, id: %r>' % (self.username, self.id)

    # Return the JSON representation of the User model
    def to_json(self):
        return json.dumps({
            'id': self.id,
            'username': self.username
            })


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    is_completed = db.Column(db.Integer, default=0)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    # Return the string representation of the Todo model (debugging)
    def __repr__(self):
        return '<Desc %r, id: %r>' % (self.description, self.id)

    # Return the JSON representation of the Todo model
    def to_json(self):
        return json.dumps({
            'id': self.id,
            'description': self.description,
            'is_completed': self.is_completed,
            'user_id': self.user_id
            })
