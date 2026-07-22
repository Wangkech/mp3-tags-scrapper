from pathlib import Path
from mutagen import MutagenError
from mutagen.mp3 import EasyMP3, HeaderNotFoundError
from mutagen.easyid3 import EasyID3, EasyID3KeyError
import math
import time


# path = Path.home()/"Music/Music"
music_dir = Path.cwd()/"music"
start_time = time.time()

def scan_music (path):
    files = []
    for file in path.iterdir():
        if file.is_file() and  file.suffix.lower() in ['.mp3']:
        # if file.is_file() and  file.suffix in ['.mp3','m4a', '.wav', '.flac']:
            files.append(file)
    return files


def print_tags(files):
    for file in files:
        audio_file = EasyMP3(file) 
        try:
            audio_file.pprint(audio_file.tags())
            print(f"{files.index(file) + 1} {file.name}")
            print("Title: ", audio_file.get("title"))
            print("Artist: ", audio_file.get("artist"))
            print("Album: ", audio_file.get("album"))
            print()
        except HeaderNotFoundError or EasyID3KeyError or MutagenError: 
            print(f"{files.index(file) + 1} {file.name}")
            print("Title: ", audio_file.get("title"))
            print("Artist: ", audio_file.get("artist"))
            print("Album: ", audio_file.get("album"))
            print()



# scan_music(music_dir)

files = scan_music(music_dir)
for file in files:
    
        file_size = file.stat().st_size /  (1024 * 1024)
        audio_file = EasyMP3(file)
        tags = EasyID3(file)
        duration = int(audio_file.info.length) / 60
        duration_mins = math.floor(duration)
        duration_secs = (duration - duration_mins) * 60

        print(f"{files.index(file) + 1} {file.name}")
        print(f"     Extension:  {file.suffix.lower()}")
        print(f"     Size:  {file_size:.2f} MB")
        print(f"     duration: {duration_mins}mins { duration_secs:.0f}s")
        try:
            if tags:
                print(f"     Has Tags: Yes")
        except EasyID3KeyError : 
            if not tags:
                print(f"     Has Tags: No")
        
# # files = scan_music(path)
# # print_tags(files)
# print_tags(files)


        
print()
print(f"scanned all files in {(time.time() - start_time)*1000:.3f} milliseconds ")

    