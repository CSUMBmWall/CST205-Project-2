from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from mutagen._file import File

'''
This class sets the ID3 tags for downloaded song
'''
class ID3:

    def __init__(self, info, newFileName):

        #set new filename from user entered info
        trackInfo = info['artist'] + " - " + info['album'] + " - " + info['title']
        newFileName = info['directory'] + "/" + trackInfo + ".mp3"
        filePath = newFileName

        #check if tags exist and set
        try:
            download = EasyID3(filePath)
        except ID3NoHeaderError:
            download = File(filePath, easy=True)
            download.add_tags()

        #set tags from user info
        download['title'] = info['title']
        download['artist'] = info['artist']
        download['album'] = info['album']
        download.save()

