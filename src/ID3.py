from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from mutagen._file import File



filePath = "D:\Downloads\Music\Johnny Flynn and Laura Marling - YouTube -  The Water.mp3"

try:
    meta = EasyID3(filePath)
except ID3NoHeaderError:
    meta = File(filePath, easy=True)
    meta.add_tags()

meta['title'] = "The Water"
meta['artist'] = "Johnny Flynn and Laura Marling"
meta['genre'] = "Indie"
meta['album'] = "Youtube"
meta.save()
print(meta)

'''
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from mutagen._file import File



filePath = "D:\Downloads\Music\Johnny Flynn and Laura Marling - YouTube -  The Water.mp3"

try:
    meta = EasyID3(filePath)
except ID3NoHeaderError:
    meta = File(filePath, easy=True)
    meta.add_tags()

meta['title'] = "The Water"
meta['artist'] = "Johnny Flynn and Laura Marling"
meta['genre'] = "Indie"
meta['album'] = "Youtube"
meta.save()
print(meta)'''