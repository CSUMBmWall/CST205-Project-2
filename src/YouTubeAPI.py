import os
import subprocess
from subprocess import check_output
from youtube_dl import *

class YouTubeAPI:

    def __init__(self, info):
        self.checkInputs(info)

        #get video info from YouTube
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ytInfo = ydl.extract_info('https://www.youtube.com/watch?v=Hn1BapsppXM')

        print('Title of the extracted video/playlist: %s' % ytInfo['title'])
        downloadFileName = info['directory'] + "/" + str(ytInfo['title']) + ".mp3"
        print(downloadFileName)

        #run the youtube_dl command to download video
        osCommand = "youtube-dl --extract-audio --audio-format mp3 -o " + info['directory'] + "/%(title)s.%(ext)s " + info['url']
        os.system(osCommand)


        trackInfo = info['artist'] + " - " + info['album'] + " - " + info['title']
        newFileName =  info['directory'] + "/" + trackInfo + ".mp3"
        print("newFileName - " + newFileName)

        os.rename(downloadFileName, newFileName)

    def checkInputs(self, info):
        for entry in info:
            if info[entry] is None:
                info[entry] = ''