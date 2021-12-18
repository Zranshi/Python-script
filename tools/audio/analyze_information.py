# -*- coding: UTF-8 -*-
# @Time     : 2021/11/03 19:12
# @Author   : Ranshi
# @File     : analyze_information.py
# @Doc      : 分析wav音频信息
import json
import wave

from utils.file import FilePath


def analyze_audio(audio: str) -> dict:
    """
    analyze_audio 分析wav音频信息

    通过文件路径分析获得wav文件的基础信息, 包括文件相关和音频相关的信息.

    Args:
        audio (str): 音频文件信息.

    Returns:
        dict: 打印一个包含文件信息的字典.
    """
    audio: FilePath = FilePath(audio)
    if audio.file_ext != ".wav":
        raise ValueError(f"'{audio.path}' 不是一个wav文件.")
    with wave.open(audio, "rb") as wav:
        params = wav.getparams()
    data = {
        "File Name": audio.file_name,
        "Filename Extension": audio.file_ext,
        "Absolute path": audio.path,
        "nchannels": params[0],
        "sampwidth": params[1],
        "framerate": params[2],
        "nframes": params[3],
    }
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    analyze_audio(
        audio="/Users/rs/Downloads/test.wav",
    )
