from flask import Flask, render_template

app = Flask(__name__)

articles = {
    1: {},
    2: {},
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
