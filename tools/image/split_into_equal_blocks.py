#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/24 17:30
# @Author   : Ranshi
# @File     : split_into_equal_blocks.py
# @Doc      : 拆分一个图片为多个相等的块, 可自定义长和宽分别为多少块.
import os

from PIL import Image
from utils.file import FilePath


def split_image_into_equal_blocks(
    img_path: str,
    row: int,
    col: int,
    line_width: int = 1,
    is_save_part_img: bool = False,
    is_save_line_split_img: bool = True,
    target_path: str = None,
):
    """
    split_image_into_equal_blocks 将一个图片拆分为多个相同的块.

    Args:
        img_path (str): 源图片路径
        row (int): 行数
        col (int): 列数
        line_width (int, optional): 分割线的宽度. Defaults to 1.
        is_save_part_img (bool, optional): 是否将各个块分别保存为文件. Defaults to False.
        is_save_line_split_img (bool, optional): 是否将用分割线划分的图片保存为图片. Defaults to True.
        target_path (str, optional): 输出图片的路径. Defaults to None.
    """
    img_path: FilePath = FilePath(img_path)
    img = Image.open(img_path)
    # dir, file = os.path.split(img_path)
    # file_name = os.path.splitext(file)[0]
    if target_path is None:
        target_path = img_path.owned_folder

    width, height = img.size
    height_step, width_step = height / row, width / col
    idx_row, idx_col = 0, 0

    block_lst: list[list[Image.Image]] = []
    while idx_row < height:
        idx_col = 0
        line_lst: list[Image.Image] = []
        while idx_col < width:
            box = (idx_col, idx_row, idx_col + width_step, idx_row + height_step)
            block = img.crop(box)
            line_lst.append(block)
            idx_col += width_step
        block_lst.append(line_lst)
        idx_row += height_step

    if is_save_part_img:
        parts_dir = f"{target_path}/{img_path.file_name}-parts"
        if not os.path.exists(parts_dir):
            os.mkdir(parts_dir)
        part_num = 1
        for line_list in block_lst:
            for img in line_list:
                img.save(f"{parts_dir}/part_{part_num}.jpg")
                part_num += 1

    if is_save_line_split_img:
        new_width, new_height = int(width_step + 0.5), int(height_step + 0.5)
        new_img = Image.new(
            "RGB",
            (new_width * col + (col - 1) * line_width, new_height * row + (row - 1) * line_width),
            (255, 255, 255),
        )
        for i in range(len(block_lst)):
            for j in range(len(block_lst[0])):
                new_img.paste(
                    block_lst[i][j],
                    (
                        j * new_width + j * line_width,
                        i * new_height + i * line_width,
                    ),
                )
        new_img.save(f"{target_path}/{img_path.file_name}-line-split.jpg")


if __name__ == "__main__":
    split_image_into_equal_blocks(
        img_path="/Users/rs/Downloads/818F7D55870FF1E444AA669FC9C8ADB9.jpg",
        row=3,
        col=7,
    )
