from app import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'Id': self.id,
            'Title': self.title,
            'Content': self.content,
            'Category': self.category,
            'Created_date': self.created_date,
            'Updated_date': self.updated_date,
            'Status': self.status
        }
    
    def __repr__(self):
        return f'<Post {self.name}>'