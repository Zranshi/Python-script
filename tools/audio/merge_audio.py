from moviepy.editor import AudioFileClip, concatenate_audioclips
from utils.file import FilePath


def merge_audio(file_list: list[str], target_path: str = None):
    audio_path_list: list[FilePath] = [FilePath(file_name) for file_name in file_list]
    if target_path is None:
        target_path: FilePath = FilePath(
            f"{audio_path_list[0].owned_folder}/{audio_path_list[0].file_name}-merge.mp3"
        )
    audio_list = []
    for file_path in audio_path_list:
        if file_path.file_ext == ".mp3":
            audio_list.append(AudioFileClip(file_path.path))
    concatenate_audioclips(audio_list).write_audiofile(target_path.path)
