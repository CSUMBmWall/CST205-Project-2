from __future__ import unicode_literals

import uuid

import shutil
import youtube_dl


class Ydl:
    def __init__(self, options):
        self.options = options

    def setOptions(self):

        self.ydlOptions = {
            'format': 'bestaudio/best',
            'outtmpl' : '%options[artist]s - %options[album]s options[title].%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        #return ydlOptions

    def downloadVideo(self):
        with youtube_dl.YoutubeDL(self.ydlOptions) as ydl:
            ydl.download(self.options[url])


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

testURL = "https://www.youtube.com/watch?v=w5IOou6qN1o"

options =           {'url': testURL,
                    'artist': 'Muddy Waters',
                    'album' : 'YouTube',
                    'title' : 'MannishBoy',
                    'directory': 'D:/Downloads'
                    }

testYDL = Ydl(options)
testYDL.downloadVideo()
