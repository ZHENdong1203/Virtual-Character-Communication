from flask import Blueprint, request, jsonify, session, make_response
from extensions import bcrypt
from db import SessionLocal
from models import User, RememberToken
from datetime import datetime
from config import REMEMBER_COOKIE_NAME, REMEMBER_COOKIE_DURATION
import urllib.parse
import random

auth_bp = Blueprint("auth", __name__)

def get_random_dicebear_avatar(username: str) -> str:
    """
    生成随机头像，使用dicebear的API
    :param username:
    :return:
    """
    styles = ['icons', 'shapes', 'thumbs', 'bottts-neutral', 'fun-emoji']
    style = random.choice(styles)
    seed = f"{username}_{random.randint(1000, 9999)}"
    encoded_seed = urllib.parse.quote_plus(seed)
    return f"https://api.dicebear.com/9.x/{style}/svg?seed={encoded_seed}"

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    登录接口，会判断是否勾选记住我
    :return:
    """
    data = request.json
    username = data.get("username", "").strip()
    password = data.get("password", "")
    remember_me = data.get("remember_me", False)

    db = SessionLocal()
    user = db.query(User).filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"success": False, "message": "用户名或密码错误"}), 401

    # 生成头像
    if not user.avatar_url:
        user.avatar_url = get_random_dicebear_avatar(user.username)
        db.commit()

    resp = make_response(jsonify({"success": True, "message": "登录成功"}))

    if remember_me:
        token_str = RememberToken.generate_token()
        expires_at = datetime.utcnow() + REMEMBER_COOKIE_DURATION
        token = RememberToken(user_id=user.id, token=token_str, expires_at=expires_at)
        db.add(token)
        db.commit()

        resp.set_cookie(
            REMEMBER_COOKIE_NAME,
            token_str,
            max_age=REMEMBER_COOKIE_DURATION.total_seconds(),
            httponly=True,
            samesite="Lax"
        )
    else:
        session["user_id"] = user.id

    return resp

@auth_bp.route("/logout", methods=["POST"])
def logout():
    """
    注销接口
    :return:
    """
    db = SessionLocal()
    token_str = request.cookies.get(REMEMBER_COOKIE_NAME)

    if token_str:
        token = db.query(RememberToken).filter_by(token=token_str).first()
        if token:
            db.delete(token)
            db.commit()

    session.pop("user_id", None)

    resp = make_response(jsonify({"success": True, "message": "已退出登录"}))
    resp.delete_cookie(REMEMBER_COOKIE_NAME)
    return resp


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    注册接口
    :return:
    """
    data = request.json
    username = data.get("username", "").strip()
    password = data.get("password", "")
    captcha = data.get("captcha", "")
    session_captcha = session.get("captcha_code")

    if not session_captcha or captcha.lower() != session_captcha.lower():
        return jsonify({"success": False, "message": "验证码错误"})

    db = SessionLocal()
    try:
        existing_user = db.query(User).filter_by(username=username).first()
        if existing_user:
            return jsonify({"success": False, "message": "用户名已存在"})

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, password=hashed_pw)
        db.add(new_user)
        db.commit()

        return jsonify({"success": True, "message": "注册成功"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": f"注册失败：{str(e)}"})
    finally:
        db.close()
