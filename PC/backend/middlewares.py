from flask import g, request, session
from db import SessionLocal
from models import User, RememberToken
from datetime import datetime
from config import REMEMBER_COOKIE_NAME

"""
全局中间件
"""
def load_user():
    """
    登录时是否勾选记住我
    :return:
    """
    g.user = None
    db = SessionLocal()
    user_id = session.get("user_id")

    if user_id:
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            g.user = user
            return

    token_str = request.cookies.get(REMEMBER_COOKIE_NAME)
    if token_str:
        token = db.query(RememberToken).filter_by(token=token_str).first()
        if token and token.expires_at > datetime.utcnow():
            g.user = token.user
