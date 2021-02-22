from flask import Flask, render_template, request
from categories import categories
from article import articles, find_by_text

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', articles=articles, categories=categories)


@app.route('/article/<int:art>')
def article(art):
    return render_template('article.html', article=articles[art - 1], categories=categories)


@app.route('/categories/<int:cat>')
def categor(cat):
    return render_template('categories.html', articles=articles, categor=categories[cat - 1], categories=categories)


@app.route('/search')
def search():
    text = request.args['text']
    return render_template('index.html', categories=categories, articles=find_by_text(text))


@app.route('/login')
def singin():
    return render_template('login.html')


@app.route('/singin')
def singup():
    return render_template('singin.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', articles=articles, categories=categories), 404


if __name__ == '__main__':
    app.run()
