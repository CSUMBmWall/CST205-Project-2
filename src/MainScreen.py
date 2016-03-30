from tkinter import *
from tkinter import filedialog
from YouTubeAPI import *


class MainScreen:

    def __init__(self, master):
        self.directory = ""

        master.minsize(width=600, height=400)
        #master.configure(background="firebrick3")
        frame = Frame(master)

        urlLabel = Label(frame, text="URL")
        artistLabel = Label(frame, text="Artist")
        albumLabel = Label(frame, text="Album")
        titleLabel = Label(frame, text="Title")
        directoryLabel = Label(frame, text="Directory")


        urlEntry = Entry(frame, width=50)
        artistEntry = Entry(frame, width=50)
        albumEntry = Entry(frame, width=50)
        albumEntry.insert(0, "YouTube")
        titleEntry = Entry(frame, width=50)
        directoryEntry = Entry(frame, width=50)

        urlLabel.grid(row=0, sticky=E)
        artistLabel.grid(row=1, sticky=E)
        albumLabel.grid(row=2, sticky=E)
        titleLabel.grid(row=3, sticky=E)
        directoryLabel.grid(row=4, sticky=E)

        urlEntry.grid(row=0, column=1)
        artistEntry.grid(row=1, column=1)
        albumEntry.grid(row=2, column=1)
        titleEntry.grid(row=3, column=1)
        directoryEntry.grid(row=4, column=1)

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
        self.directoryEntry.insert(0, self.directory)

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



