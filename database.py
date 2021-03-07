from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=True)
    mail = db.Column(db.String(70), nullable=True, unique=True)
    password = db.Column(db.String(70), nullable=True)
    admin_field = db.Column(db.Boolean, default=False)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=True)
    body = db.Column(db.String(70), nullable=True, unique=True)
    date = db.Column(db.String(70), nullable=True)
    big = db.Column(db.Boolean, default=True)
    img = db.Column(db.Boolean, default=False)
    img_url = db.Column(db.String(70))
    author = db.Column(db.Integer)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)