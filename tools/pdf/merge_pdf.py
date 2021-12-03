#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/02 23:09
# @Author   : Ranshi
# @File     : merge_pdf.py
# @Doc      : 合并PDF
from PyPDF2.pdf import PdfFileReader, PdfFileWriter
from utils.file import FilePath


def merge_pdf(source_path_lst: list[str] = list(), target_path: str = ""):
    """
    merge_pdf 合并pdf.

    Args:
        source_path_lst (list[str], optional): 源文件路径数组. Defaults to list().
        target_path (str, optional): 目标文件路径. Defaults to "".
    """
    target_pdf = PdfFileWriter()
    for path in source_path_lst:
        file_path: FilePath = FilePath(path)
        source_pdf = PdfFileReader(file_path.path)
        target_pdf.appendPagesFromReader(source_pdf)
    with open(target_path, "wb") as target_file:
        target_pdf.write(target_file)


if __name__ == "__main__":
    merge_pdf(
        source_path_lst=[],
        target_path="",
    )
