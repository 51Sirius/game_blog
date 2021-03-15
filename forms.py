from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea, TextInput, PasswordInput


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()], widget=TextInput())
    body = StringField('Текст статьи', validators=[DataRequired()], widget=TextArea())
    category_id = IntegerField('ID Категории', validators=[DataRequired()], widget=TextInput('number'))
    author_id = IntegerField('ID Автора', validators=[DataRequired()], widget=TextInput('number'))
    image = StringField('Ссылка на картинку', validators=[DataRequired()], widget=TextInput())


class Registration(FlaskForm):
    nickname = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    mail = StringField('Почта', validators=[DataRequired()], widget=TextInput())
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())


class Login(FlaskForm):
    mail_or_name = StringField('Ник или почта', validators=[DataRequired()], widget=TextInput())
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())