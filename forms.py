from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()])
    body = StringField('Текст статьи', validators=[DataRequired()])
    category_id = IntegerField('ID Категории', validators=[DataRequired()])
    author_id = IntegerField('ID Автора', validators=[DataRequired()])