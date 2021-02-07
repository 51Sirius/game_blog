from flask import Flask, render_template

app = Flask(__name__)

articles = {
    1: {},
    2: {},
}


@app.route('/')
def homepage():
    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    app.run()
