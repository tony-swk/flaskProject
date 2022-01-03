from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return 'SPACEWALK Home'


@app.route('/user')
def user():
    return 'Hello User, this is user page of  SPACEWALK'


if __name__ == '__main__':
    app.run()
