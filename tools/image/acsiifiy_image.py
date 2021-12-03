#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/02 23:16
# @Author   : Ranshi
# @File     : acsiifiy_image.py
# @Doc      : 将图片转换成字符画
import numpy as np
from alive_progress import alive_bar
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

SYMBOLS = np.array([" ", ".", "L", "O", "V", "E"])


def save_as_image(arr, out_path: str, font, new_im_size, colors):
    letter_size = font.getsize("x")
    im_out_size = new_im_size * letter_size
    bg_color = "black"
    im_out = Image.new("RGB", tuple(im_out_size), bg_color)
    draw = ImageDraw.Draw(im_out)

    y = 0
    with alive_bar(len(arr) * len(arr[0]), bar="classic2", title=out_path.split("/")[-1]) as bar:
        for i, line in enumerate(arr):
            for j, ch in enumerate(line):
                color = tuple(colors[i, j])
                draw.text((letter_size[0] * j, y), ch[0], fill=color, font=font)
                bar()
            y += letter_size[1]
    im_out = ImageEnhance.Brightness(im_out).enhance(1.25)
    im_out = ImageEnhance.Color(im_out).enhance(1.25)
    im_out.save(out_path)


def ascii_art(source_path: str, out_path: str, rate: int):
    """
    ascii_art 绘制字符画.

    Args:
        source_path (str): 源文件夹目录.
        out_path (str): 输出文件夹目录.
        rate (int): 字符画比率.

    Returns:
        list: 字符画数组.
    """
    im = Image.open(source_path)
    font = ImageFont.load_default()
    aspect_ratio = font.getsize("x")[0] / font.getsize("x")[1]
    new_im_size = np.array([im.size[0], im.size[1] * aspect_ratio]).astype(int)

    while max(new_im_size) > rate:
        new_im_size[0] //= 1.2
        new_im_size[1] //= 1.2

    im = im.resize(new_im_size)
    im_color = np.array(im)
    im = im.convert("L")

    im = np.array(im)

    im = (im - im.min(initial=None)) / (im.max(initial=None) - im.min(initial=None))
    im *= SYMBOLS.size - 1
    ascii_ch = SYMBOLS[im.astype(int)]

    save_as_image(ascii_ch, out_path, font, new_im_size, im_color)

    return "\n".join(("".join(r) for r in ascii_ch))


if __name__ == "__main__":
    ascii_art(
        source_path="",
        out_path="",
        rate=300,
    )
