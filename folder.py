from pathlib import Path
from mutagen.easyid3 import EasyID3, EasyID3KeyError

from MusicFile import Song, Metadata

class Folder: 
    def __init__(self, path):
        self.path =  path
        self.name = self.path.name
        self.songs = self.get_songs()

    def get_songs(self):
        files = []
        for file in self.path.iterdir():
            if file.suffix in ['.mp3','.m4a','.flac','.wav']:              
                files.append(Song(file))
        return files
