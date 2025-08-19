from .auth import auth_bp
from .user import user_bp
from .captcha import captcha_bp
from .chat import chat_bp

"""
注册蓝图
"""
def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(captcha_bp, url_prefix="/captcha")
    app.register_blueprint(chat_bp, url_prefix="/chat")
