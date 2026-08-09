from pathlib import Path

path = Path.cwd()

def print_tags(song):
    print("=== Tags ====")
    try:
        metadata = song.metadata
        if metadata:
            print("Title: ", metadata.title)
            print("Artist: ", metadata.artist)
            print("Album: ", metadata.album)
    except:
        print("This song has no metadata")
    print()



def print_folder_details(folder):
    print(f"folder path: {folder.path}")
    print(f"folder name: {folder.name}")
    print(f"songs found: { len(folder.songs)}")
    print(f"complete tags: { len(folder.complete_tags)}")
    print(f"partial tags: { len(folder.partial_tags)}")
    print(f"no tags: { len(folder.no_tags)}")
    print()

def print_song_details(song):
    print(f" { song.name }")
    print(f"Extension: {song.extension}")
    print(f"size: {song.size:.2f}MB")
    print(f"length: {song.length}")
    print(f"status: {song.status}")
    # print_tags(song)

def write_folder_details(folder, report):
    report.write(f"folder path: {folder.path}\n")
    report.write(f"folder name: {folder.name}\n")
    report.write(f"songs found: { len(folder.songs)}\n")
    report.write("\n")

def write_tags(song, report):
    try:
        metadata = song.metadata
        if metadata:
            report.write(f"Title:  {metadata.title}\n")
            report.write(f"Artist:  {metadata.artist}\n")
            report.write(f"Album: { metadata.album}\n")
    except:
        report.write("This song has no metadata\n")
    report.write("\n")

def write_song_details(song, report):
    report.write(f"{ song.name }\n")
    report.write(f"Extension: {song.extension} \n")
    report.write(f"size: {song.size:.2f}MB\n")
    report.write(f"length: {song.length}\n")
    report.write(f"status: {song.status}\n")
    report.write("=== Tags ====\n")
    # write_tags(song)

def generate_report(folder):
    with open("report.txt", "w") as report:
        write_folder_details(folder,report)
        songs = folder.songs
        for song in songs:
            write_song_details(song,report)
            write_tags(song, report)
        
def print_report(folder):
    print_folder_details(folder)
    songs = folder.songs
    for song in songs:
        print_song_details(song)
        print_tags(song)
   