import os
from youtube_dl import *
from mutagen.ID3 import *

'''
This class utilizes youtube-dl to download mp3 from YouTube
'''

class YouTubeAPI:

    def __init__(self, info):
        self.chekGUIfieldsForNone(info)

        #get video info from YouTube
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            ytInfo = ydl.extract_info(info['url'])

        #set downloaded filename
        downloadFileName = info['directory'] + "/" + str(ytInfo['title']) + ".mp3"

        #run the youtube_dl command to download video
        osCommand = "youtube-dl --extract-audio --audio-format mp3 -o " + info['directory'] + "/%(title)s.%(ext)s " + info['url']
        os.system(osCommand)

        #use info from gui to create new filname and rename
        trackInfo = info['artist'] + " - " + info['album'] + " - " + info['title']
        newFileName =  info['directory'] + "/" + trackInfo + ".mp3"
        os.rename(downloadFileName, newFileName)

        #set ID3 tag
        ID3(info, newFileName)


    def chekGUIfieldsForNone(self, info):
        for entry in info:
            if info[entry] is None:
                info[entry] = ''