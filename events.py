import os
from watchdog.events import RegexMatchingEventHandler
import subdb, utils

class VideoEventHandler(RegexMatchingEventHandler):
    VIDEO_REGEX = [r".*(mkv|avi|mp4|m4v)$"]

    def __init__(self):
        super().__init__(self.VIDEO_REGEX)

    def on_created(self, event):
        print(f"! new video => {event.src_path}")
        self.rename_original_subtitles(event)
        self.get_subtitles(event)

    def rename_original_subtitles(self, event):
        filename, ext = os.path.splitext(event.src_path)
        if os.path.isfile(f"{filename}.srt"):
            os.rename(f"{filename}.srt",f"{filename}.original.srt")

    def get_subtitles(self, event):
        s = subdb.SubDb(event.src_path)
        available_languages = s.get_available_languages()
        s.download(utils.get_prefered_language(available_languages))
