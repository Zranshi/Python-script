# Python-script

一个 Python 编写的用于日常文件操作的命令行工具.

## 依赖

- 用于将函数转为命令行指令的依赖: fire
- 用于处理图片的库: Pillow
- 用于处理音频和视频的库: pydub, moviepy
- 用于处理 pdf 的库: PyPDF2
- 用于绘制图像和处理矩阵的库: matplotlib, numpy
- 用于绘制进度条的库: alive_progress

详细版本见 requirements.txt

## 功能

- analyze_audio 分析 wav 音频信息
- draw_spectrogram 绘制频谱图
- draw_spectrum 绘制光谱图.
- draw_waveform_graph 绘制波形图
- convert_mp3_2_wav 将 mp3 文件转换成 wav 文件.
- video_2_audio 提取视频中的音频.
- ascii_art 绘制字符画.
- split_image_into_equal_blocks 将一个图片拆分为多个相同的块.
- merge_pdf 合并 pdf.
- split_max_10MB 拆分 pdf 文件, 最大为 10MB.
- split_pdf 拆分 PDF.
- change_text 文本文件替换.
- merge_audio 合并音频.
