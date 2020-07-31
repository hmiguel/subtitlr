import requests, re
import utils
from pathlib import Path

class SubDb(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.hash = utils.get_hash(file_path)

    def get_available_languages(self):
        return self.__request("search").decode('utf-8').split(",")
    
    def download(self, lang):
        with open(Path(self.file_path).with_suffix('.srt'), 'wb') as f:
            f.write(self.__request("download", lang))

    def __request(self, action, language = None):
        url = f"http://api.thesubdb.com/?action={action}&hash={self.hash}" + (f"&language={language}" if language else "")
        header = {"user-agent": "SubDB/1.0 (subtitlr/1.0; https://github.com/hmiguel/subtitlr.git)"}
        print(f"subdb request {action} : {url}")
        req = requests.get(url, headers=header)
        if req.status_code != 200:
            raise Exception(f'SubDub exception: {req.status_code}')
        return req.content 
            