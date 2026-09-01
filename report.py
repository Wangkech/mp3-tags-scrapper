from pathlib import Path

path = Path.cwd()
report = path / "report.txt"


def get_tags_format(metadata):
    try:
        tags_format = f"=== Tags ====\nTitle: {metadata.title}\nArtist: {metadata.artist}\nAlbum: {metadata.album}\n"
        return tags_format
    except:
        return None


def get_song_details_format(song):
    song_details_format = f"\n{ song.name }\nExtension: {song.extension}\nsize: {song.size:.2f}MB\nlength: {song.length}\nstatus: {song.status}\n"
    return song_details_format


def get_folder_details_format(folder):
    folder_details_format = f"folder path: {folder.path}\nfolder name: {folder.name}\nsongs found: { len(folder.songs)}\ncomplete tags: { len(folder.complete_tags)}\npartial tags: { len(folder.partial_tags)}\nno tags: { len(folder.no_tags)}\n\n"
    return folder_details_format


def print_tags(song):
    metadata = song.metadata
    print(get_tags_format(metadata))


def print_folder_details(folder):
    print(get_folder_details_format(folder))


def print_song_details(song):
    print(get_song_details_format(song))


def write_folder_details(folder):
    with open(report, "a", encoding="utf-8") as file:
        file.writelines(get_folder_details_format(folder))


def write_tags(song):
    metadata = song.metadata
    with open(report, "a", encoding="utf-8") as file:
        format = get_tags_format(metadata)
        format = format if format else f"This song has no metadata\n\n"
        file.write(format)


def write_song_details(song):
    with open(report, "a", encoding="utf-8") as file:
        try:
            file.write(get_song_details_format(song))
        except UnicodeEncodeError:
            report.write_text(f"could encode these characters")
    # write_tags(song)


def generate_report(folder):
    with open(report, "w", encoding="utf-8") as file:
        file.write("\n")
    write_folder_details(folder)
    songs = folder.songs
    for song in songs:
        write_song_details(song)
        write_tags(song)


def print_report(folder):
    print_folder_details(folder)
    songs = folder.songs
    for song in songs:
        print_song_details(song)
        print_tags(song)
