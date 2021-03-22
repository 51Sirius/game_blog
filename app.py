from flask import Flask, render_template, request, redirect, url_for, abort
from database import db, Users, Article, Categories, find_by_text
from flask_migrate import Migrate
from forms import ArticleForm, Registration, Login
from flask_wtf import form
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import datetime
import locale
from os import environ

locale.setlocale(locale.LC_ALL, '')
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


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
    articles = find_by_text(text, articles)
    if articles is None:
        return render_template('errors/404.html', categories=categories), 404
    return render_template('index.html', categories=categories, articles=articles)


@app.route('/singin', methods=['GET', 'POST'])
def singin():
    log_form = Login()
    if log_form.validate_on_submit():
        email_nick = log_form.mail_or_name.data
        password = log_form.password.data
        user = Users.query.filter_by(mail=email_nick).first()
        print(user, user.check_password(password))
        if not (user and user.check_password(password)):
            abort(403)
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.errorhandler(404)
def not_found(error):
    categories = Categories.query.all()
    articles = Article.query.all()
    return render_template('errors/404.html', articles=articles, categories=categories), 404


@app.route('/create_article', methods=['GET', 'POST'])
@login_required
def create_article():
    categories = Categories.query.all()
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        title = article_form.title.data
        body = article_form.body.data
        category_id = article_form.category_id.data
        author_id = current_user.id
        image = article_form.image.data
        date = datetime.datetime.now().strftime('%d.%m..%Y')
        if image is not None or image != '':
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
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
