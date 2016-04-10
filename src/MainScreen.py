from tkinter import *
from tkinter import filedialog
from YouTubeAPI import *

'''
This class is used to set up GUI that asks user for the
YouTube url, Artist Name, Album(defaults to YouTube), and song title
instantiates YouTubeApi with this info on user submit
'''

class MainScreen:

    def __init__(self, root):

        root.minsize(width=420, height=175)
        root.configure(background="black")
        root.wm_title("Youtube Downloader and ID tagger")
        frame = Frame(root)
        frame.configure(background = "black")

        #set up Labels
        self.urlLabel = Label(frame, text="URL", fg = "chartreuse", bg = "black" )
        self.artistLabel = Label(frame, text="Artist", fg = "chartreuse", bg = "black")
        self.albumLabel = Label(frame, text="Album", fg = "chartreuse", bg = "black")
        self.titleLabel = Label(frame, text="Title", fg = "chartreuse", bg = "black")
        self.directoryLabel = Label(frame, text="Directory", fg = "chartreuse", bg = "black")

        #set up Entry boxes
        self.urlEntry = Entry(frame, width=50, bg = "chartreuse", highlightbackground = "black", fg = "black")
        self.artistEntry = Entry(frame, width=50, bg = "chartreuse", highlightbackground = "black", fg = "black")
        self.albumEntry = Entry(frame, width=50, bg = "chartreuse", highlightbackground = "black", fg = "black")
        self.albumEntry.insert(0, "YouTube")
        self.titleEntry = Entry(frame, width=50, bg = "chartreuse", highlightbackground = "black", fg = "black")
        self.directoryEntry = Entry(frame, width=50, bg = "chartreuse", highlightbackground = "black", fg = "black")

        #place labels in grid
        self.urlLabel.grid(row=1, sticky=E)
        self.artistLabel.grid(row=2, sticky=E)
        self.albumLabel.grid(row=3, sticky=E)
        self.titleLabel.grid(row=4, sticky=E)
        self.directoryLabel.grid(row=5, sticky=E)

        #place entry boxes in grid
        self.urlEntry.grid(row=1, column=1)
        self.artistEntry.grid(row=2, column=1)
        self.albumEntry.grid(row=3, column=1)
        self.titleEntry.grid(row=4, column=1)
        self.directoryEntry.grid(row=5, column=1)

        #create buttons
        chooseDirectory = Button(frame, text="Browse", command=self.askUserForDirectory, relief ="groove", fg ="chartreuse", bg ="black", activebackground ="chartreuse", activeforeground ="black")
        quitButton = Button(frame, text="Quit", command=frame.quit, relief="groove", fg="chartreuse", bg="black", activebackground="chartreuse", activeforeground="black")
        enterButton = Button(frame, text="Download", command=self.submit, relief="groove", fg="chartreuse", bg="black", activebackground="chartreuse", activeforeground="black")

        #place buttons
        chooseDirectory.grid(row=5, column = 2, sticky=N+S)
        enterButton.grid(row=6, column=1, sticky=E+W)
        quitButton.grid(row=7, column=1, sticky=E+W)

        frame.pack()

        frame.mainloop()

    def askUserForDirectory(self):
        directory = filedialog.askdirectory()
        self.directoryEntry.insert(0, directory)

    def submit(self):
        url = self.urlEntry.get()
        #testYDL = Ydl(url, setOptions())
        #downloadVideo(testYDL)

        #create dictionary to store track information from user
        userInfo = {'url': self.urlEntry.get(),
                    'artist': self.artistEntry.get(),
                    'album': self.albumEntry.get(),
                    'title': self.titleEntry.get(),
                    'directory': self.directoryEntry.get()
                    }

        YouTubeAPI(userInfo)


