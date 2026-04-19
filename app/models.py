from . import db
from flask_login import UserMixin
import secrets

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    api_token =db.Column(db.String(100), default=lambda: secrets.token_hex(16))
    profile_pic = db.Column(db.String(200), default="default.jpg")
    post = db.relationship("Post", backref = "author", lazy =True)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    content =db.Column(db.Text)
    user_id =db.Column(db.Integer, db.ForeignKey("user.id"))



    