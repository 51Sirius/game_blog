from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=True)
    mail = db.Column(db.String(70), nullable=True, unique=True)
    password = db.Column(db.String(70), nullable=True)