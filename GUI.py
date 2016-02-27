from tkinter import *
from tkinter import filedialog


class MainScreen:
    def __init__(self, master):
        self.directory = ""

        master.minsize(width=600, height=400)
        frame = Frame(master)

        self.artistLabel = Label(frame, text="Artist")
        self.albumLabel = Label(frame, text="Album")
        self.titleLabel = Label(frame, text="Title")
        self.directoryLabel = Label(frame, text="Directory")

        self.artistEntry = Entry(frame, width=50)
        self.albumEntry = Entry(frame, width=50)
        self.titleEntry = Entry(frame, width=50)
        self.directoryEntry = Entry(frame, width=50)

        self.artistLabel.grid(row=0, sticky=E)
        self.albumLabel.grid(row=1, sticky=E)
        self.titleLabel.grid(row=2, sticky=E)
        self.directoryLabel.grid(row=3, sticky=E)

        self.artistEntry.grid(row=0, column=1)
        self.albumEntry.grid(row=1, column=1)
        self.titleEntry.grid(row=2, column=1)
        self.directoryEntry.grid(row=3, column=1)


        self.chooseDirectory = Button(frame, text="Browse", command=self.askDirectory)
        self.chooseDirectory.grid(row=3, column = 2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(columnspan=3)


        frame.pack()

    def askDirectory(self):
        self.directory = filedialog.askdirectory()
        self.directoryEntry.insert(0, self.directory)

root = Tk()
button = MainScreen(root)
root.mainloop()

