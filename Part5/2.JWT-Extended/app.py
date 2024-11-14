from flask import Flask, render_template, request, redirect
from jwt_utils import configure_jwt
from routes.user import user_blp
# from flask_jwt_extended import JWTManager

# app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
# jwt = JWTManager(app)

app = Flask(__name__)
configure_jwt(app)

app.register_blueprint(user_blp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)