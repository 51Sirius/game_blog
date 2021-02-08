from flask import Flask, render_template

app = Flask(__name__)

articles = {
    1: {'title': 'Gaming It',
        'text': 'В следующем месяце Disco Elysium дебютирует на консолях и получит расширенную версию — The Final Cut. Среди нововведений — политические квесты, о которых во время анонса нового издания разработчики почти ничего не говорили. Зато поговорили в интервью Push Square.',
        'date': '08.02.2021'
        },
    2: {'title': 'Gaming IT',
        'text': 'В следующем месяце Disco Elysium дебютирует на консолях и получит расширенную версию — The Final Cut. Среди нововведений — политические квесты, о которых во время анонса нового издания разработчики почти ничего не говорили. Зато поговорили в интервью Push Square.',
        'date': '09.02.2021'},
}

categories = {
    1: {'name': 'Lost Ark'},
    2: {'name': 'GTA'},
    3: {'name': 'Game Dev'},
    4: {'name': 'Steam'},
    5: {'name': 'Company'}
}


@app.route('/')
def homepage():
    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    app.run()
