from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Youtube')
Label(root, text = 'Youtube').pack()

link = StringVar()
Label(root, text = 'Link').place(x = 225,y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root,text = 'Downloaded',font = 'arial 15').place(x = 180, y = 210)
Button(root,text = 'Download',command = Downloader).place(x = 190, y = 150)
root.mainloop()


