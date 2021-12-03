#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/03 19:26
# @Author   : Ranshi
# @File     : mp3_2_wav.py
# @Doc      : 将mp3文件转换成wav文件
from pydub import AudioSegment
from utils.file import FilePath


def convert_mp3_2_wav(mp3_path: str) -> None:
    """
    convert_mp3_2_wav 将mp3文件转换成wav文件.

    Args:
        mp3_path (str): mp3文件路径.
    """
    mp3: FilePath = FilePath(mp3_path)
    if mp3.file_ext != ".mp3":
        raise ValueError(f"'{mp3_path}' Not an mp3 file.")

    AudioSegment.from_mp3(mp3_path).export(f"{mp3.owned_folder}/{mp3.file_name}.wav", format="wav")


if __name__ == "__main__":
    convert_mp3_2_wav(
        mp3_path="/Users/rs/Downloads/test_file.mp3",
    )
