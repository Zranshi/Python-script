# -*- coding: UTF-8 -*-
# @Time     : 2021/12/01 19:21
# @Author   : Ranshi
# @File     : extract_audio_from_video.py
# @Doc      : 提取视频中的音频
from moviepy.editor import AudioFileClip
from utils.file import FilePath


def video_2_audio(file_path: str, target_path: str = None):
    """
    video_2_audio 提取视频中的音频.

    将视频的音频提取出来, 另存为一个文件.

    Args:
        file_path (str): 视频路径
        target_path (str, optional): 音频保存路径, 若未设置则默认为视频路径和视频名称. Defaults to None.
    """
    file_path = FilePath(file_path)
    target_path = (
        FilePath(target_path)
        if target_path
        else FilePath(f"{file_path.owned_folder}/{file_path.file_name}.mp3")
    )
    audio_clip = AudioFileClip(file_path.path)
    audio_clip.write_audiofile(target_path.path)


if __name__ == "__main__":
    video_2_audio(file_path=FilePath("/Users/rs/Downloads/必背！肖秀荣1000题速刷版(附带背音频) - 005 - 毛中特.mp4"))
