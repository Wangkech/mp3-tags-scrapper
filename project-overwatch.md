# Problem   
The problem is personal. I am someone who loves music. At the same time i like having my music offline  on my phone and PC in form of portable files that i can carry and play on any device.   

However, for a longtime i have been dealing with cases whereby i happen to like a song and want to listen to the full album only to realise that i actually have to google the song, write down the album, again google the album then manually put the songs - of which most of the time I always happen to be having in music files - to a playlist, then play it. That strategy used to work but it was time consuming and it wasn't reliable as i always had to do it for every manually.  I would end up with a very long list of playlist. 

Now try do the same manually on the other devices. Not sustainable! Let's say something happens such as mistakenly clearing the data and cache of my music app and just like that my manually create playlists are gone - we are back to zero.

And how about when I bump into a good artist and feel like only listeng to that artist and get hit with the classic "Unkown Artist"? I would write a whole book on this but in short, lets just said these ruined my experience with music files.

The only option i had was to either redownload the thousands of songs from a good source - which would cost crazy data and time - or either edit the tags manually using a tags editor tool - again, that would take forever. 

So here comes the not yet named "mp3-tags-scrapper" tool...   


## The Not Yet Named "mp3-tags-scrapper" tool   

with this tool you should be able to:   
1. use partially available data about the song such as:-
    - file name or the loosely available metadata  to do an online look up to find the right metadata and edit the metadata of the song.

2. If the song file has no metadata and has no metadata, then the audio itself will be used to look up the data about it online.

3. fix randomized song file names with a defined prefer format i.e 
    -  "song_title - artist ft featured_artist & another_featured_artist" or 
    - " artsist ft featured_artist & another_featured_artist - song_title" or
    -   any future supported formats. 


# TECHNICALITY
* This project's core will be entirely based on python.
# Critical Modules
## Mutagen
* this is the enabling module for dealing with tags metadata when it comes to determining the validity of the said music file, extracting tags and editing tags.  

## Other regular inbuilt modules:
1. pathlib
2. os modules
3. re for cleaning texts

# API's
1. ## MusicBrainz  
* MusicBrainz has a robust database for tracks metadata. it offers free api access. 

2. ## AcoustID
* this will be my go to for dealing with songs that have literaly no metadata and have a misleading filename. 

## Approach
* I shall be using the OOP approach where we shall have objects such as:   
    1. Folder   
        * **Responsibility**   
            * scanning for legit music files
            * categorising files based on their statuses i.e. (corrupt, has_partial_tags, has_complete_tags, has_no_tags)
            * MusicFile reports directly to it.
    2. MusicFile
        * **Responsibility**   
            * know about it's tags status
            * should know how to rename itself
            * know its file data
            * know its path
            * reports its state to Folder
            * metadata object report to it

    3. tags/metadata
        * **Responsibility**   
            * extract it's tags
            * edit tags
            * reports to the MusicFile/song object

* main.py will be the coordinator. 


# WHAT I HAVE ACHIEVED SO FAR:
Lets start from the smallest object as we progress upwards.  
1. METADATA obj
    - can extract available tags from the metadeta:-
        - title
        - artist
        - album artist
        - album
        - year 
    - returns null for the unavailable tags and entirely null if there are no available metadata    

2. MusicFile / Song class
    - Based on the data from the metadata it stores it and:
        - tags itself complete if the it has full defined tags    
        - considers itself partial if there it has only title and artist
        - no tags if it completely has no tags. 
    - if the file is not a valid music file then it will tags it self as an error incidicating corruptness.
    - right now we can use ```Song.rename() ``` to rename the filename of the music file for songs that have full metadata. the format i'm currently using is "artist - title" and "artist ft co-artist - title"

    - we have cleaning in place to clean the title extracted from the embedded metadata incase it contains things such as the artist name or popular unwanted tags such as [official, music, video,audio, lyrics, lyrics, 128k, 128kb, etc]
    
3. Folder class
    - scans all the files in the folder for musics files and categorizes them into their states. [error, no tags, complete, partitial]
    - it now now initiates the renaming of the songs with complete tags.  

4. report.py 
    - generates a written report on the findings of the folder and documents what files we renamed and what we they renamed to. "from ====> to"
    - write how