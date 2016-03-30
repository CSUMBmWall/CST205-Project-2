import youtube_dl
import os
import MainScreen
from tkinter import *
from tkinter import filedialog
from youtubedlAPI import *

root = Tk()

app = MainScreen(root)

extractAudio = '--extract-audio'
audioFormat = '--audio-format mp3'

os.system("youtube-dl --extract-audio --audio-format mp3 -o C:\\Users\Matt\Downloads\Music\%(title)s.%(ext)s(uploader) https://www.youtube.com/watch?v=Hn1BapsppXM")