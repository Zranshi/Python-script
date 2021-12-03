#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/08 19:18
# @Author   : Ranshi
# @File     : split_into_10MB_pdf.py
# @Doc      : 将一个pdf拆分为固定大小的文件.(最小拆分单位为10MB)
import os

from PyPDF2 import PdfFileReader, PdfFileWriter

TMP = "/Users/rs/Downloads/.Temporary_pdf"  # 临时文件名称
MAX_SIZE = 10  # 分割后每个文件最大大小, 单位为MB


def __reorganization(
    source_path: str,
    target_path: str,
    pages=list[int],
):
    target_pdf = PdfFileWriter()
    with open(source_path, "rb") as source_file:
        source_pdf = PdfFileReader(source_file)
        for page in pages:
            if 0 <= page < source_pdf.getNumPages():
                target_pdf.addPage(source_pdf.getPage(page))
        with open(target_path, "wb") as target_file:
            target_pdf.write(target_file)


def is_right_file_size(file_path: str, left, right) -> bool:
    __reorganization(source_path=file_path, target_path=TMP, pages=list(range(left, right)))
    file_size = os.path.getsize(TMP)
    return file_size < 1000 ** 2 * MAX_SIZE


def split_max_10MB(file_path: str):
    """
    split_max_10MB 拆分pdf文件, 最大为10MB.

    Args:
        file_path (str): pdf文件路径.
    """

    def bisect_search_page(left, right):
        lo, hi = left, right
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if is_right_file_size(file_path, left, mid):
                if not is_right_file_size(file_path, left, mid + 1):
                    return mid
                else:
                    lo = mid + 1
            else:
                hi = mid - 1
        return lo

    if not os.path.isfile(file_path):
        raise ValueError(f"'{file_path}' 不存在.")
    if os.path.splitext(file_path)[-1] != ".pdf":
        raise ValueError(f"'{file_path}' 不是pdf文件.")
    file_idx, left = 0, 0
    with open(file_path, "rb") as source_file:
        page_num = PdfFileReader(source_file).getNumPages()
    while left < page_num:
        right = (
            page_num
            if is_right_file_size(file_path, left, page_num)
            else bisect_search_page(left, page_num)
        )
        __reorganization(
            source_path=file_path,
            target_path=os.path.splitext(file_path)[0] + f"_{file_idx}.pdf",
            pages=list(range(left, right)),
        )
        left = right
        file_idx += 1
    os.remove(TMP)


if __name__ == "__main__":
    split_max_10MB("")
