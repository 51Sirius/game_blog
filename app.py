from flask import Flask, render_template, request, redirect, url_for, abort
from article import find_by_text
from database import db, Users, Article, Categories
from flask_migrate import Migrate
from forms import ArticleForm, Registration, Login
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ

locale.setlocale(locale.LC_ALL, '')
app = Flask(__name__)
app.secret_key = b'+dw4124rafa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)


@app.route('/')
def homepage():
    articles = Article.query.all()
    categories = Categories.query.all()
    return render_template('index.html', articles=articles, categories=categories)


@app.route('/article/<int:art>')
def article(art):
    article = Article.query.filter_by(id=art).first_or_404()
    categories = Categories.query.all()
    return render_template('article.html', article=article, categories=categories)


@app.route('/categories/<int:cat>')
def categor(cat):
    articles = Article.query.all()
    categories = Categories.query.all()
    return render_template('categories.html', articles=articles, categor=categories[cat - 1], categories=categories)


@app.route('/search')
def search():
    text = request.args['text']
    articles = Article.query.all()
    categories = Categories.query.all()
    return render_template('index.html', categories=categories, articles=find_by_text(text, articles))


@app.route('/singin')
def singin():
    log_form = Login()
    if log_form.validate_on_submit():
        pass
    return render_template('login.html', form=log_form)


@app.route('/register', methods=['GET', 'POST'])
def singup():
    register_form = Registration()
    if register_form.validate_on_submit():
        email = register_form.mail.data
        name = register_form.nickname.data
        password = register_form.password.data
        existing_user = Users.query.filter_by(mail=email).first()
        if existing_user:
            abort(400)
        user = Users(name=name, mail=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('singup.html', form=register_form)


@app.errorhandler(404)
def not_found(error):
    categories = Categories.query.all()
    articles = Article.query.all()
    return render_template('errors/404.html', articles=articles, categories=categories), 404


@app.route('/create_article', methods=['GET', 'POST'])
def create_article():
    categories = Categories.query.all()
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        title = article_form.title.data
        body = article_form.body.data
        category_id = article_form.category_id.data
        author_id = article_form.author_id.data
        image = article_form.image.data
        date = datetime.datetime.now().strftime('%d.%m..%Y')
        if image is not None:
            img = True
        else:
            img = False
        if len(body) > 300:
            big_body = True
        else:
            big_body = False
        article = Article(title=title, body=body, category_id=category_id, author_id=author_id, img=img, img_url=image,
                          big=big_body, date=date)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('new_article.html', form=article_form, categories=categories)


if __name__ == '__main__':
    app.run()
