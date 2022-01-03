from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return '''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문</p>
    <a href="https://www.naver.com">Naver 홈페이지 바로가기</a>
    '''


@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name} ({user_id})'


if __name__ == '__main__':
    app.run()
