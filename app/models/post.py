from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Post(db.Model):
    __tablename__ = 'posts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    style = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    caption = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
    imageUrl = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    comments = db.relationship('Comment', backref='post', cascade='all, delete-orphan')

    @property
    def get_userId(self):
        return self.userId

    @property
    def get_comments(self):
        return [comment.to_dict() for comment in self.comments]

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'style': self.style,
            'size': self.size,
            'price': str(round(self.price,2)),  # Convert Decimal to string for JSON
            'caption': self.caption,
            'available': self.available,
            'imageUrl': self.imageUrl,
            'createdAt': self.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt': self.updatedAt.strftime('%Y-%m-%d %H:%M:%S'),
            'comments': [comment.to_dict() for comment in self.comments],
        }


    # not sure if i need this, need to review routes
    def delete(self):
        db.session.delete(self)
