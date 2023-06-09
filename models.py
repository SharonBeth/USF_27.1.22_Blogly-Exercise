"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

db = SQLAlchemy()

def connect_db(app):
    """Connet to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """Users"""
    
    __tablename__ = 'users'

    # Example from videos
    @classmethod
    def get_user_by_id(cls, id):
        cls.query.filter_by(id=id).all()
    
    # Example from videos
    # def __repr__(self):
        # p = self
        # return f"XXXXXXXX"
    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name ={u.first_name} last_name={u.last_name} image_url={u.image_url}>"
    id          = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    first_name  = db.Column(db.String(25),
                            nullable=True)
    last_name   = db.Column(db.String(25),
                            nullable=True)
    image_url   = db.Column(db.String,
                            nullable=True)

 
