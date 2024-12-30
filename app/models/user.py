from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    is_artist = db.Column(db.Boolean, nullable=False, default=True)
    profileImageUrl = db.Column(db.String)
    bio = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='user', cascade='all, delete-orphan')
    # add bookings and messages if time allows

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'is_artist': self.is_artist,
            'profileImageUrl': self.profileImageUrl if self.profileImageUrl else "",
            'bio': self.bio if self.bio else "",
            'createdAt': self.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt': self.updatedAt.strftime('%Y-%m-%d %H:%M:%S'),
            'posts': [post.to_dict() for post in self.posts],
            'comments': [comment.to_dict() for comment in self.comments],
        }
