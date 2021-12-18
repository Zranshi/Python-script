# -*- coding: UTF-8 -*-
# @Time     : 2021/12/01 19:24
# @Author   : Ranshi
# @File     : file.py
# @Doc      : 文件路径相关工具
import os
from enum import Enum

EXT_MAPPING = (
    {".txt"},
    {".jpg", ".png"},
    {".mp3", ".wav"},
    {".mp4", ".avi"},
    {".pdf", ".html"},
    {".db"},
    {".xml", ".json", ".toml", ".yaml"},
)


class FileType(Enum):
    TEXT = 0
    IMAGE = 1
    AUDIO = 2
    VIDEO = 3
    PAGE = 4
    DATA = 5
    TABLE = 6
    OTHER = 7

    @classmethod
    def get_type(cls, ext: str) -> "FileType":
        for i, v in enumerate(EXT_MAPPING):
            if ext in v:
                return FileType(i)
        return FileType.OTHER


class FilePath(object):
    def __init__(self, file_path: str) -> "FilePath":
        self.path = file_path
        self.owned_folder, self.file_all_name = os.path.split(self.path)
        self.file_name, self.file_ext = os.path.splitext(self.file_all_name)
        self.file_type: FileType = FileType.get_type(self.file_ext)

        if not os.path.exists(self.owned_folder):
            raise FileExistsError("Folder does not exist.")
