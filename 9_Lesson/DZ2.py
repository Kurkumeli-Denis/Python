
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

def Downloader_video():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root,text = 'Downloaded',font = 'arial 15').place(x = 180, y = 210)
Button(root,text = 'Download video',command = Downloader_video).place(x = 190, y = 150)


def Downloader_audio():
    url = YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).desc().first()
    audio.download()
    Label(root,text = 'Downloaded',font = 'arial 15').place(x = 180, y = 210)
Button(root,text = 'Download audio',command = Downloader_audio).place(x = 190, y = 200)


root.mainloop()