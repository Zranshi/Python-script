# -*- coding: UTF-8 -*-
# @Time     : 2021/11/02 21:46
# @Author   : Ranshi
# @File     : split_pdf.py
# @Doc      : 拆分PDF
from string import Template

from PyPDF2 import PdfFileReader, PdfFileWriter


def __reorganization(
    source_path: str,
    target_path: str,
    pages=list[int],
):
    """
    重组 PDF 的 IO 操作函数, 将 pages 中的所有页面数(合法) 拆分为一个新的PDF.

    Args:
        source_path (str): 源文件路径
        target_path (str): 目标文件路径
        pages ([type], optional): 需要的pages. Defaults to list[int].
    """
    target_pdf = PdfFileWriter()
    with open(source_path, "rb") as source_file:
        source_pdf = PdfFileReader(source_file)
        for page in pages:
            if 0 <= page < source_pdf.getNumPages():
                target_pdf.addPage(source_pdf.getPage(page))
        with open(target_path, "wb") as target_file:
            target_pdf.write(target_file)


def split_step(start, end, step):
    for i in range(start, end, step):
        yield list(range(i, i + step))


def split_pieces(start, end, piece):
    total = end - start
    step = total // piece if total > piece else 1
    for i in range(start, end, step):
        yield list(range(i, i + step))


def split_mark_points(start, end, points):
    points = sorted(list(set(points) | {end} - {start}))
    idx = start
    for point in points:
        yield list(range(idx, point))
        idx = point


def split_pdf(
    source_path: str,
    target_path: str = None,
    diff_name: Template = Template("${path}_part-${num}"),
    start: int = 0,
    end: int = None,
    mod: str = "step",
    arg=None,
):
    """
    split_pdf 拆分PDF.

    有三种拆分方式:
    1. 一共分成几块.
    2. 以几页一组.
    3. 以特定的几组点分割数组.

    Args:
        source_path (str): 源文件路径
        target_path (str, optional): 目标文件路径. Defaults to None.
        diff_name (Template, optional): part 后缀模版. Defaults to Template("_part-").
        start (int, optional): 开始页面. Defaults to 0.
        end (int, optional): 结束页面. Defaults to None.
        mod (str, optional): 拆分模式. Defaults to "piece".

    Raises:
        ValueError: [description]
    """
    if end is None:
        with open(source_path, "rb") as source_file:
            end = PdfFileReader(source_file).getNumPages()

    if target_path is None:
        target_path = ".".join(source_path.split(".")[:-1])

    if mod == "piece":
        if arg is None:
            arg = 4

        gen = split_pieces(start, end, arg)
    elif mod == "points":
        gen = split_mark_points(start, end, arg)
    elif mod == "step":
        if arg is None:
            arg = 20
        gen = split_step(start, end, arg)
    else:
        raise ValueError("Unknown mod for split PDF")

    for part, pages in enumerate(gen):
        __reorganization(
            source_path=source_path,
            target_path=diff_name.substitute(path=target_path, num=part) + ".pdf",
            pages=pages,
        )


if __name__ == "__main__":
    split_pdf(
        source_path="/Users/rs/Downloads/12-hypothesis-Practical Statistics for Field Biology_wrapper(1).pdf",
        target_path=None,
        start=0,
        end=None,
        mod="step",
        arg=1,
    )
