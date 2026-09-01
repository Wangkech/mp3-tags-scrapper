from MusicFile import Song
from pathlib import Path

renamed_report = Path.cwd() / "success_report.txt"


class Folder:
    def __init__(self, path):
        self.path = path
        self.name = self.path.name
        self.songs = self.get_songs()
        self.complete_tags = []
        self.partial_tags = []
        self.no_tags = []
        self.error = []

        self.arrange_songs()

    def get_songs(self):
        files = []
        for file in self.path.iterdir():
            if file.suffix.lower() in [".mp3", ".m4a", ".flac", ".wav"]:
                files.append(Song(file))
        return files

    def arrange_songs(self):
        for song in self.songs:
            if song.tag_status == "complete":
                self.complete_tags.append(song)
            elif song.tag_status == "partial":
                self.partial_tags.append(song)
            else:
                self.no_tags.append(song)

    def rename_complete_songs(self, dir):
        for song in self.complete_tags:
            old_name = song.name
            new_name = song.rename(dir)

            print(f"{old_name} ===> {new_name}")
