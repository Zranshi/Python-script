# -*- coding: UTF-8 -*-
# @Time     : 2021/11/03 13:02
# @Author   : Ranshi
# @File     : change_text.py
# @Doc      : 替换所有文件中的对应文本
import os


def dirs_files(path: str, ignore: list[str]) -> list:
    res = []
    if path.split("/")[-1] in ignore:
        return []
    if os.path.isdir(path):
        for next_path in os.listdir(path):
            res += dirs_files(f"{path}/{next_path}", ignore)
    else:
        res.append(path)
    return res


def change_text(source_dir_path: str, replaced_str: str, target_str: str, ignore: list[str]):
    """
    change_text 文本文件替换.

    Args:
        source_dir_path (str): 源文件目录.
        replaced_str (str): 替换字符.
        target_str (str): 目标字符.
        ignore (list[str]): 忽略.

    """
    if not os.path.exists(source_dir_path):
        raise ValueError(f"不存在'{source_dir_path}'")
    for file in dirs_files(source_dir_path, ignore):
        with open(file, "r+") as f:
            content = f.readlines()
        for idx, item in enumerate(content):
            content[idx] = item.replace(replaced_str, target_str)
        with open(file, "w+") as f:
            f.writelines(content)


if __name__ == "__main__":
    change_text(
        source_dir_path="/Users/rs/Downloads/rs-leetcode/interview-classic",
        replaced_str="Hello World",
        target_str="你好, 世界",
        ignore=[".git", ".DS_Store"],
    )
