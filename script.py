# -*- coding: UTF-8 -*-
# @Time     : 2021/12/07 21:12
# @Author   : Ranshi
# @File     : script.py
# @Doc      : 非命令行形式的运行方式, 直接以脚本调用形式工作.

from tools import split_pdf

split_pdf(
    source_path="/Users/rs/Downloads/Gutiérrez-Rodríguez et al_2016_SR of CCFP in China_EnvEvid.pdf",
    mod="step",
    arg=11,
)
