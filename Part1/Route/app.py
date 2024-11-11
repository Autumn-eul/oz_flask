from flask import Flask, request, Response
import test

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main Page!"

# 복사할 코드를 선택 후 Option + Shift + 화살표 위/아래 : 위/아래로 복사
@app.route('/about')
def about():
    return "This is the about page!"


# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# http://127.0.0.1:5000/user/choonsik
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'


# post 요청 날리는 법
# (1) postman
# (2) requests

import requests # 없으면 pip install requests

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url = url, data = data)

    return Response("Sucessfully submitted", status = 200)


@app.route('/submit', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print('GET method')

    if request.method == 'POST':
        print("***POST method***", request.data)


# 파라미터를 숫자로만 받고 싶을 땐
@app.route('/number/<int:number>')
def number(number):
    return f'Number : {number}'




