from flask import Blueprint, session, send_file
from PIL import Image, ImageDraw, ImageFont
import random, string, io

captcha_bp = Blueprint("captcha", __name__)

def generate_code(length=4):
    """
    生成四位验证码数字
    :param length:
    :return:
    """
    return ''.join(random.choices(string.digits, k=length))

def generate_captcha_image(code):
    """
    生成验证码图片，四位数字加干扰线
    :param code: 验证码显示的四位数字
    :return:
    """
    width, height = 100, 40
    image = Image.new("RGB", (width, height), (255, 255, 255))
    font = ImageFont.truetype("arial.ttf", 24)
    draw = ImageDraw.Draw(image)

    # 绘制验证码数字
    for i, char in enumerate(code):
        x = 10 + i * 20
        y = random.randint(0, 10)
        draw.text((x, y), char, font=font, fill=(random.randint(0, 100), 0, random.randint(0, 100)))

    # 干扰线
    for _ in range(5):
        x1, y1, x2, y2 = [random.randint(0, d) for d in (width, height, width, height)]
        draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0), width=1)

    return image


@captcha_bp.route("/get-pic", methods=["GET"])
def captcha():
    """
    生成验证码接口
    :return:
    """
    code = generate_code()
    session["captcha_code"] = code
    image = generate_captcha_image(code)

    buf = io.BytesIO()
    image.save(buf, "PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")
