from pathlib import Path
from mutagen import MutagenError
from mutagen.mp3 import EasyMP3, HeaderNotFoundError
from mutagen.easyid3 import EasyID3, EasyID3KeyError
import math
import time

from folder import Folder


start_time = time.time()
dir = Path.cwd()/"music"
print(dir.name)
song_folder = Folder(dir)

def print_tags(song):

    metadata = song.metadata
    if metadata:
        print("Title: ", metadata.title)
        print("Artist: ", metadata.artist)
        print("Album: ", metadata.album)
        print()
    if not metadata:
        print("This song has no metadata")
        print()


def print_folder_details():
    print("folder path: ",song_folder.path)
    print("folder name: ",song_folder.name)
    print("songs found: " , len(song_folder.songs))

songs = song_folder.songs
def print_song_details():
    for song in songs:
        print(f"{ song.name }")
        print(f"Extension: {song.extension}")
        print(f"size: {song.size}")
        print(f"length: {song.length}")
        print("=== Tags ====")
        print_tags(song)

print_folder_details()
print()
print_song_details()

        
print()
print(f"scanned in {(time.time() - start_time)*1000:.3f} milliseconds ")


    