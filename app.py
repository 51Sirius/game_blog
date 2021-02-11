from flask import Flask, render_template
from categories import categories
from article import articles

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


if __name__ == '__main__':
    app.run()
