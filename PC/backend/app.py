from flask import Flask
from flask_cors import CORS
from extensions import bcrypt
from routes import register_routes
from middlewares import load_user

def create_app():
    app = Flask(__name__)
    app.secret_key = "anitalk"
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

    # 初始化扩展
    bcrypt.init_app(app)

    # 注册蓝图
    register_routes(app)

    # 注册中间件
    app.before_request(load_user)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
