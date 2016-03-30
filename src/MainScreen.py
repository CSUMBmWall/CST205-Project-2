from tkinter import *
from tkinter import filedialog
from YouTubeAPI import *


class MainScreen:

    def __init__(self, master):

        master.minsize(width=600, height=400)
        #master.configure(background="firebrick3")
        frame = Frame(master)

        self.urlLabel = Label(frame, text="URL")
        self.artistLabel = Label(frame, text="Artist")
        self.albumLabel = Label(frame, text="Album")
        self.titleLabel = Label(frame, text="Title")
        self.directoryLabel = Label(frame, text="Directory")

        self.urlEntry = Entry(frame, width=50)
        self.artistEntry = Entry(frame, width=50)
        self.albumEntry = Entry(frame, width=50)
        self.albumEntry.insert(0, "YouTube")
        self.titleEntry = Entry(frame, width=50)
        self.directoryEntry = Entry(frame, width=50)

        self.urlLabel.grid(row=0, sticky=E)
        self.artistLabel.grid(row=1, sticky=E)
        self.albumLabel.grid(row=2, sticky=E)
        self.titleLabel.grid(row=3, sticky=E)
        self.directoryLabel.grid(row=4, sticky=E)

        self.urlEntry.grid(row=0, column=1)
        self.artistEntry.grid(row=1, column=1)
        self.albumEntry.grid(row=2, column=1)
        self.titleEntry.grid(row=3, column=1)
        self.directoryEntry.grid(row=4, column=1)

        chooseDirectory = Button(frame, text="Browse", command=self.askDirectory)
        chooseDirectory.grid(row=4, column = 2)

        enterButton = Button(frame, text="Enter", command=self.submit)
        enterButton.grid(row=5, columnspan=1)

        quitButton = Button(frame, text="Quit", command=frame.quit)
        quitButton.grid(row=5, columnspan=4)


        frame.pack()

        frame.mainloop()

    def askDirectory(self):
        directory = filedialog.askdirectory()
        self.directoryEntry.insert(0, directory)

    def submit(self):
        url = self.urlEntry.get()
        #testYDL = Ydl(url, setOptions())
        #downloadVideo(testYDL)
        userInfo = {'url': self.urlEntry.get(),
                    'artist': self.artistEntry.get(),
                    'album': self.albumEntry.get(),
                    'title': self.titleEntry.get(),
                    'directory': self.directoryEntry.get()
                    }

        YouTubeAPI(userInfo)


#root = Tk()

#app = MainScreen(root)

# keeps the window on the screen
#root.mainloop()



