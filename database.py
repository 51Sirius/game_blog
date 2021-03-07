from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=True)
    mail = db.Column(db.String(70), nullable=True, unique=True)
    password = db.Column(db.String(70), nullable=True)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=True)
    body = db.Column(db.String(70), nullable=True, unique=True)
    date = db.Column(db.String(70), nullable=True)
    big = db.Column(db.Boolean, default=True)
    img = db.Column(db.Boolean, default=False)
    img_url = db.Column(db.String(70))


class Categories(db.Model):
    pass