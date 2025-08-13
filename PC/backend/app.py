from PIL import Image, ImageDraw, ImageFont
import random
import io
import string
from flask_cors import CORS
from flask import Flask, request, jsonify, make_response, g, session, send_file
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import Session
from models import User, RememberToken
from db import SessionLocal
from datetime import datetime, timedelta
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()  # 读取 .env 文件

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
app.secret_key = 'anitalk'  # 用于加密 session


REMEMBER_COOKIE_NAME = 'remember_token'
REMEMBER_COOKIE_DURATION = timedelta(days=30)
bcrypt = Bcrypt(app)

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.json
    confirm_password = data.get('confirmPassword')
    user_id = int(data.get('userId'))

    if user_id is None or user_id == 0:
        return jsonify(success=False, message="用户不存在")
    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    hashed_pw = bcrypt.generate_password_hash(confirm_password).decode('utf-8')

    user.password = hashed_pw
    db.commit()

    return jsonify(success=True, message="密码修改成功")

@app.route('/change-username', methods=['POST'])
def change_username():
    data = request.json
    username = data.get('userName')
    user_id = int(data.get('userId'))

    if user_id is None or user_id == 0:
        return jsonify(success=False, message="用户不存在")
    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.username = username
    db.commit()
    return jsonify(success=True, message="用户名修改成功")


@app.route('/change-avatar', methods=['POST'])
def change_avatar():
    data = request.get_json()
    avatar_url = data.get('avatarUrl')
    user_id = int(data.get('userId'))

    if not avatar_url:
        return jsonify(success=False, message="头像 URL 不能为空")

    if user_id is None or user_id == 0:
        return jsonify(success=False, message="用户不存在")
    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    user.avatar_url = avatar_url
    db.commit()

    return jsonify(success=True)
@app.route('/me', methods=['GET'])
def get_current_user():
    if not g.user:
        return jsonify({'loggedIn': False}), 401
    return jsonify({
        'loggedIn': True,
        'username': g.user.username,
        'avatarUrl': g.user.avatar_url,
        'userId': g.user.id
    })

def get_random_dicebear_avatar(username: str) -> str:
    styles = ['icons', 'shapes', 'thumbs', 'bottts-neutral', 'fun-emoji']
    style = random.choice(styles)
    seed = f"{username}_{random.randint(1000, 9999)}"
    encoded_seed = urllib.parse.quote_plus(seed)
    return f"https://api.dicebear.com/9.x/{style}/svg?seed={encoded_seed}"

# 登录接口
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    remember_me = data.get('remember_me', False)

    db: Session = SessionLocal()
    user = db.query(User).filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'success': False, 'message': '用户名或密码错误'}), 401

    # 生成头像
    if not user.avatar_url:
        user.avatar_url = get_random_dicebear_avatar(user.username)
        db.commit()

    resp = make_response(jsonify({'success': True, 'message': '登录成功'}))

    if remember_me:
        # 生成 token
        token_str = RememberToken.generate_token()
        expires_at = datetime.utcnow() + REMEMBER_COOKIE_DURATION
        token = RememberToken(user_id=user.id, token=token_str, expires_at=expires_at)
        db.add(token)
        db.commit()

        # 设置持久cookie
        resp.set_cookie(
            REMEMBER_COOKIE_NAME,
            token_str,
            max_age=REMEMBER_COOKIE_DURATION.total_seconds(),
            httponly=True,  # 前端 JS 无法访问，提高安全
            samesite='Lax'  # 根据需求改成 'Strict' 或 'None' + secure
        )
    else:
        session['user_id'] = user.id

    return resp

# 请求前验证登录状态（示例中用 remember_token 验证）
@app.before_request
def load_user():
    g.user = None
    db: Session = SessionLocal()
    user_id = session.get('user_id')
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
        else:
            g.user = None

# 退出登录，清除 token 和 cookie
@app.route('/logout', methods=['POST'])
def logout():
    token_str = request.cookies.get(REMEMBER_COOKIE_NAME)
    db: Session = SessionLocal()
    if token_str:
        token = db.query(RememberToken).filter_by(token=token_str).first()
        if token:
            db.delete(token)
            db.commit()

    session.pop('user_id', None)

    resp = make_response(jsonify({'success': True, 'message': '已退出登录'}))
    resp.delete_cookie(REMEMBER_COOKIE_NAME)
    return resp

# 生成纯数字验证码
def generate_code(length=4):
    return ''.join(random.choices(string.digits, k=length))

# 生成验证码图片
def generate_captcha_image(code):
    width, height = 100, 40
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype("arial.ttf", 24)  # 或换为其他字体路径
    draw = ImageDraw.Draw(image)

    # 绘制验证码数字
    for i, char in enumerate(code):
        x = 10 + i * 20
        y = random.randint(0, 10)
        draw.text((x, y), char, font=font, fill=(random.randint(0, 100), 0, random.randint(0, 100)))

    # 加一些干扰线
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0), width=1)

    return image

@app.route('/captcha')
def captcha():
    code = generate_code()
    session['captcha_code'] = code  # 存入 session
    image = generate_captcha_image(code)

    # 转换为字节流返回
    buf = io.BytesIO()
    image.save(buf, 'PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # 这里调用 GPT 接口
    reply = f"这是 GPT 的回复：{user_message}"

    return jsonify({"reply": reply})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    captcha = data.get('captcha', '')
    session_captcha = session.get('captcha_code')

    if not session_captcha or captcha.lower() != session_captcha.lower():
        return jsonify({'success': False, 'message': '验证码错误'})

    db = SessionLocal()
    try:
        # 查重
        existing_user = db.query(User).filter_by(username=username).first()
        if existing_user:
            return jsonify({'success': False, 'message': '用户名已存在'})

        # 加密密码并保存
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_pw)
        db.add(new_user)
        db.commit()

        return jsonify({'success': True, 'message': '注册成功'})
    except Exception as e:
        db.rollback()
        return jsonify({'success': False, 'message': f'注册失败：{str(e)}'})
    finally:
        db.close()


@app.route("/api/test")
def test():
    return {"message": "Flask is running"}

if __name__ == "__main__":
    app.run(debug=True)