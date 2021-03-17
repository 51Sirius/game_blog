from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=True)
    mail = db.Column(db.String(70), nullable=True, unique=True)
    password = db.Column(db.String(255), nullable=True)
    admin_field = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=True)
    body = db.Column(db.String(70), nullable=True, unique=True)
    date = db.Column(db.String(70), nullable=True)
    big = db.Column(db.Boolean, default=True)
    img = db.Column(db.Boolean, default=False)
    img_url = db.Column(db.String(70))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    author = db.relationship('Users', backref=db.backref('articles', lazy=True))
    category = db.relationship('Categories', backref=db.backref('articles', lazy=True))


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)