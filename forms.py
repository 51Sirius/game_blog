from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()], widget=TextArea())
    body = StringField('Текст статьи', validators=[DataRequired()], widget=TextArea())
    category_id = IntegerField('ID Категории', validators=[DataRequired()])
    author_id = IntegerField('ID Автора', validators=[DataRequired()])