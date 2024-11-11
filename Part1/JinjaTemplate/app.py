from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title': 'Flask Jinja Template', # key 값 = 변수명
        'user': 'inseop',
        'is_admin': True,
        'item_list': ['Item1', 'Item2', 'Item3']
    }

    # (1) rendering 할 html 파일명 입력
    # (2) html 로 넘겨줄 데이터 입력
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug = True) # 서버를 껐다 켜지 않아도 반영이 되게 해줌