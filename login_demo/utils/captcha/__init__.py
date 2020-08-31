#!/usr/bin/env python
# coding=utf-8

# 创建验证码
from PIL import Image, ImageDraw, ImageFont,ImageFilter
import random

"""
Image: 创建画布
ImageDraw : 创建画笔
ImageFont: 画笔字体
ImageFilter: 滤镜效果,模糊效果
"""

class Captcha():
    size = (30*4,  40)


    # 生成随机字母，根据ASCII表中得到的数据65-90为A-Z的大写字母
    @classmethod
    def __gene_rnd_char(cls):
        return chr(random.randint(65, 90))

    # 生成颜色
    @classmethod
    def __gene_rnd_color_1(cls):
        return   (random.randint(64,255),random.randint(64,255),random.randint(64,255))

    #
    @classmethod
    def __gene_rnd_color_2(cls):
        return  (random.randint(32,127),random.randint(32,127),random.randint(32,127))


    # 生成验证码
    # 使用类方法
    @classmethod
    def gene_graph_captcha(cls):
        # 验证码高和宽
        width, height = cls.size
        # 创建图片
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 验证码字体
        font = ImageFont.truetype(font='./Hack-Regular.ttf', size=24)
        # 创建画笔
        draw = ImageDraw.Draw(image)
        # 填充
        for x in range(width):
            for y in range(height):
                draw.point((x,y), fill=cls.__gene_rnd_color_1())

        text = []
        # 输出文字
        for t in range(4):
            # 第一个参数是文本的左上角
            temp = cls.__gene_rnd_char()
            draw.text(( 30*t + 10,8), temp, font=font, fill=cls.__gene_rnd_color_2())
            text.append(temp)

        # 模糊
        image = image.filter(ImageFilter.GaussianBlur(radius=1))
        return (text, image)


if __name__ == '__main__':
    img = Captcha.gene_graph_captcha()
    print(img[0])
    img[1].save('code.png', 'png')