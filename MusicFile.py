from mutagen.mp3 import EasyMP3, HeaderNotFoundError
from mutagen import File
from mutagen.easyid3 import EasyID3, EasyID3KeyError
from pathlib import Path
import re
import os
STATUSES = ["partial"
    ,"complete",
    "missing"
]

def clean_title(title):
    cleaned = re.sub(r'[\x00-\x1f\\/:*?"<>|]', ' ' , title)
    return cleaned.strip(' .')


def  clean_artist(artist):
    cleaned =  re.sub(r'[\/]', "&", artist)
    cleaned = re.sub(r'[\x00-\x1f\\/:*?"<>|]', "", cleaned)
    return cleaned.strip(' .')

class Metadata:
    def __init__(self, song ):
        self.artist = song.get("artist")[0]
        self.title = song.get("title")[0]
        self.album = song.get("album")[0]
        self.all_tags = [song.get("album"),song.get("title"),song.get("artist")]
        # self.year = song.year
        

class Song:
    def __init__(self,file):
        self.path = file
        self.name = file.stem
        self.extension= file.suffix.lower()
        self.size = file.stat().st_size /  (1024 * 1024)
        self.length = None
        self.status = "ok"

        try:
            self.__load_audio(file)
        except:
            self.status = "error"

        self.__get_tags(file)

    def __load_audio(self, file):
        audio = File(file)
        self.status = "ok"
        self.length =  int(audio.info.length) / 60

    def __get_tags(self,file):
        try:
            metadata = EasyID3(file)
            if metadata :
                self.metadata = Metadata(metadata)
                if None in self.metadata.all_tags:
                    self.tag_status = "partial"
                else:
                    self.tag_status = "complete"

        except: 
            self.tag_status = None
            self.metadata = None
    def  rename(self):
        dest_folder = Path.cwd()/"cleaned"
        title = self.metadata.title
        artist = self.metadata.artist
        new_name = f"{artist} - {title}{self.extension}"
        attempts = 0
        try:
            os.rename(self.path,  f"{dest_folder/new_name }")
            return new_name
        except FileExistsError:
            attempts += 1
            new_name = f"{self.metadata.title} - {self.metadata.title} ({attempts}){self.extension} "
            os.rename(self.path,f"{dest_folder/new_name}" )
            return self.name
        except :
            new_name = f"{clean_artist(artist)} - {clean_title(title)}{self.extension}"
            os.rename(self.path,  f"{dest_folder/new_name }")
        return new_name
                


