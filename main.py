from pathlib import Path
from report import generate_report,print_report
import time

from folder import Folder

def main():
    start_time = time.time()
    dir = Path.cwd()/"music/test"
    print(dir.name)
    song_folder = Folder(dir)
    generate_report(song_folder)
    print_report(song_folder)
    print()
    print(f"scanned in {(time.time() - start_time)*1000:.3f} milliseconds ")
    song_folder.rename_complete_songs()


if __name__ == "__main__":
    main()
    