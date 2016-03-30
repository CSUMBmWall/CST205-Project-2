from __future__ import unicode_literals
import youtube_dl
import os


class Ydl:
    def __init__(self, url, ydlOptions):
        self.url = url
        self.options = ydlOptions

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

def setOptions():
    title = 'test'
    ydlOptions = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    return ydlOptions

def downloadVideo(Ydl):
    newDirectory = 'C:/downloads/'
    path = os.getcwd()
    print(path)
    with youtube_dl.YoutubeDL(Ydl.options) as ydl:
       ydl.download([Ydl.url])
       print(type(ydl))
       #musicDir = os.listdir(music)
       #os.rename(musicDir, 'test')



#testURL = "https://www.youtube.com/watch?v=w5IOou6qN1o"

#testYDL = Ydl(testURL, setOptions())
#downloadVideo(testYDL)