import fire

from .audio.analyze_information import analyze_audio
from .audio.draw_audio_pictures import draw_spectrogram, draw_spectrum, draw_waveform_graph
from .audio.merge_audio import merge_audio
from .audio.mp3_2_wav import convert_mp3_2_wav
from .image.acsiifiy_image import ascii_art
from .image.split_into_equal_blocks import split_image_into_equal_blocks
from .pdf.merge_pdf import merge_pdf
from .pdf.split_into_10MB_pdf import split_max_10MB
from .pdf.split_pdf import split_pdf
from .text_file.change_text import change_text
from .video.video_2_audio import video_2_audio

__all__ = [
    "analyze_audio",
    "draw_spectrogram",
    "draw_spectrum",
    "draw_waveform_graph",
    "convert_mp3_2_wav",
    "video_2_audio",
    "ascii_art",
    "split_image_into_equal_blocks",
    "merge_pdf",
    "split_max_10MB",
    "split_pdf",
    "change_text",
    "merge_audio",
]

SCRIPT_MAPPING = {func_name: globals()[func_name] for func_name in __all__}


def run():
    fire.Fire(SCRIPT_MAPPING)
