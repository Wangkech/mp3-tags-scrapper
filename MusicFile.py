from mutagen.mp3 import EasyMP3, HeaderNotFoundError
from mutagen import File
from mutagen.easyid3 import EasyID3, EasyID3KeyError


class Song:
    def __init__(self,file):
        self.__load_audio(file)
        self.__get_tags(file)


    def __load_audio(self, file):
        audio = File(file)
        self.path = file
        self.name = file.name
        self.extension= file.suffix.lower()
        self.size = file.stat().st_size /  (1024 * 1024)
        self.length =  int(audio.info.length) / 60

    def __get_tags(self,file):
        try:
            metadata = EasyID3(file)
            if metadata :
                self.metadata = Metadata(metadata)
        except: 
            self.metadata = None




class Metadata:
    def __init__(self, song ):
        self.artist = song.get("artist")
        self.title = song.get("title")
        self.album = song.get("album")
        # self.year = song.year
        