from mutagen.mp3 import EasyMP3, HeaderNotFoundError
from mutagen import File
from mutagen.easyid3 import EasyID3, EasyID3KeyError
STATUSES = ["partial"
    ,"complete",
    "missing"
]

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
        self.status = "okay"
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




class Metadata:
    def __init__(self, song ):
        self.artist = song.get("artist")
        self.title = song.get("title")
        self.album = song.get("album")
        self.all_tags = [song.get("album"),song.get("title"),song.get("artist")]
        # self.year = song.year
        