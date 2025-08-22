from flask import Blueprint, request, jsonify, g
from extensions import bcrypt
from db import SessionLocal
from models import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/change-password", methods=["POST"])
def change_password():
    """
    用户中心修改密码
    :return:
    """
    data = request.json
    user_id = int(data.get("userId"))
    confirm_password = data.get("confirmPassword")

    db = SessionLocal()
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify(success=False, message="用户不存在")

    user.password = bcrypt.generate_password_hash(confirm_password).decode("utf-8")
    db.commit()
    return jsonify(success=True, message="密码修改成功")


@user_bp.route("/change-username", methods=["POST"])
def change_username():
    """
    用户中心修改用户名
    :return:
    """
    data = request.json
    username = data.get("userName")
    user_id = int(data.get("userId"))

    db = SessionLocal()
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify(success=False, message="用户不存在")

    user.username = username
    db.commit()
    return jsonify(success=True, message="用户名修改成功")


@user_bp.route("/change-avatar", methods=["POST"])
def change_avatar():
    """
    用户中心修改用户头像
    :return:
    """
    data = request.json
    avatar_url = data.get("avatarUrl")
    user_id = int(data.get("userId"))

    if avatar_url is None or avatar_url == "":
        return jsonify(success=False, message="头像 URL 不能为空")

    db = SessionLocal()
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify(success=False, message="用户不存在")

    user.avatar_url = avatar_url
    db.commit()
    return jsonify(success=True, message="头像修改成功")


@user_bp.route("/me", methods=["GET"])
def get_current_user():
    """
    获取当前用户信息
    :return:
    """
    if not g.user:
        return jsonify({"loggedIn": False}), 401
    return jsonify({
        "loggedIn": True,
        "username": g.user.username,
        "avatarUrl": g.user.avatar_url,
        "userId": g.user.id
    })
