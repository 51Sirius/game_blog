from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {'title': 'Gaming It',
     'text': 'В следующем месяце Disco Elysium дебютирует на консолях и получит расширенную версию — The Final Cut. Среди нововведений — политические квесты, о которых во время анонса нового издания разработчики почти ничего не говорили. Зато поговорили в интервью Push Square.',
     'date': '08.02.2021',
     'big': True,
     'id': 1
     },
    {'title': 'Gaming IT',
     'text': 'В следующем месяце Disco Elysium дебютирует на консолях и получит расширенную версию — The Final Cut. Среди нововведений — политические квесты, о которых во время анонса нового издания разработчики почти ничего не говорили. Зато поговорили в интервью Push Square.',
     'date': '09.02.2021',
     'big': False,
     'id': 2
     },
]

categories = [
    {'name': 'Lost Ark', 'id': 1},
    {'name': 'GTA', 'id': 2},
    {'name': 'Game Dev', 'id': 3},
    {'name': 'Steam', 'id': 4},
    {'name': 'Company', 'id': 5}
]


@app.route('/')
def homepage():
    return render_template('index.html', articles=articles, categories=categories)


@app.route('/article/<int:article>')
def article(article):
    return render_template('article.html', article=articles[article - 1], categories=categories)


if __name__ == '__main__':
    app.run()
