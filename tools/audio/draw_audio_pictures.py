#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/03 20:15
# @Author   : Ranshi
# @File     : draw_audio_pictures.py
# @Doc      : 绘制wav文件波形图、频谱图、语谱图
import wave

import matplotlib.pyplot as plt
import numpy as np
from utils.file import FilePath


def draw_waveform_graph(file_path: str):
    """
    draw_waveform_graph 绘制波形图

    Args:
        file_path (str): wav文件路径
    """
    file: FilePath = FilePath(file_path)
    with wave.open(file.path, "rb") as wav:
        framerate, nframes = wav.getparams()[2:4]
        data = wav.readframes(nframes)
    data = np.frombuffer(data, dtype=np.short)
    data.shape = -1, 2
    data = data.T
    time = np.arange(0, nframes) / framerate
    plt.plot(time, data[0])
    plt.xlabel("time/s")
    plt.ylabel("amplitude")
    plt.show()


def draw_spectrum(file_path: str):
    """
    draw_spectrum 绘制光谱图.

    Args:
        file_path (str): wav文件路径
    """
    file: FilePath = FilePath(file_path)
    with wave.open(file.path, "rb") as wav:
        framerate, nframes = wav.getparams()[2:4]
        data = wav.readframes(nframes)
    data = np.frombuffer(data, dtype=np.short)
    data.shape = -1, 2
    data = data.T
    df = framerate / (framerate - 1)
    freq = [df * n for n in range(framerate)]
    data = data[0][:framerate]
    c = np.fft.fft(data) * 2 / framerate

    plt.plot(freq[: round(len(freq) / 2)], abs(c[: round(len(c) / 2)]), "r")
    plt.title("Freq")
    plt.xlabel("Freq/Hz")
    plt.show()


def draw_spectrogram(file_path):
    """
    draw_spectrogram 绘制频谱图

    Args:
        file_path ([type]): wav文件路径
    """
    file: FilePath = FilePath(file_path)
    with wave.open(file.path, "rb") as wav:
        nchannels, sampwidth, framerate, nframes = wav.getparams()[:4]
        data = wav.readframes(nframes)
    data = np.frombuffer(data, dtype=np.short)
    data = data * 1.0 / max(abs(data))
    data = np.reshape(data, [nframes, nchannels]).T

    framelength = 0.025
    framesize = framelength * framerate

    lst = [32, 64, 128, 256, 512, 1024]
    nfftdict = {i: abs(framesize - i) for i in lst}
    sortlst = sorted(nfftdict.items(), key=lambda x: x[1])
    framesize = int(sortlst[0][0])

    NFFT = framesize
    overlap_size = int(round(1.0 / 3 * NFFT))
    spectrum, frep, ts, fig = plt.specgram(
        data[0],
        NFFT=NFFT,
        Fs=framerate,
        window=np.hanning(M=NFFT),
        noverlap=overlap_size,
        mode="default",
        scale_by_freq=True,
        sides="default",
        scale="dB",
        xextent=None,
    )
    plt.ylabel("Frequency")
    plt.xlabel("Time")
    plt.title("spectrogram")
    plt.show()


if __name__ == "__main__":
    draw_spectrogram(file_path="/Users/rs/Downloads/test.wav")
