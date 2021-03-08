from flask import Flask, render_template, request
from categories import categories
from article import find_by_text
from database import db, Users, Article, Categories
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    articles = Article.query.all()
    return render_template('index.html', articles=articles, categories=categories)


@app.route('/article/<int:art>')
def article(art):
    article = Article.query.filter_by(id=art).first_or_404()
    return render_template('article.html', article=article, categories=categories)


@app.route('/categories/<int:cat>')
def categor(cat):
    articles = Article.query.all()
    return render_template('categories.html', articles=articles, categor=categories[cat - 1], categories=categories)


@app.route('/search')
def search():
    text = request.args['text']
    articles = Article.query.all()
    return render_template('index.html', categories=categories, articles=find_by_text(text, articles))


@app.route('/login')
def singin():
    return render_template('login.html')


@app.route('/singin')
def singup():
    return render_template('singin.html')


@app.errorhandler(404)
def not_found(error):
    articles = Article.query.all()
    return render_template('errors/404.html', articles=articles, categories=categories), 404


if __name__ == '__main__':
    app.run()
