from tkinter import *
import os
from playsound import playsound
import pygame

windows = Tk()
windows.title("Music_Player")
windows.geometry("1000x250")

pygame.mixer.init();

track = StringVar()
status = StringVar()

sng_frame = LabelFrame(windows, text="Song Track", bg="red")
sng_frame.place(x=0, y=0, width=600, height=100)

#songtrack = Label(sng_frame, textvariable=track, width=20, font="bold", bg="Orange")
#songtrack.grid(row=0, column=0, padx=10, pady=5)

songstatus = Label(sng_frame, textvariable=status, font="bold", bg="Orange")
songstatus.grid(row=0, column=1, padx=10, pady=5)

cntrl_panel = LabelFrame(windows, text="Control Panel", width=250, height=100, bg="yellow")
cntrl_panel.place(x=0, y=100, width=600, height=100)

sng_lst = LabelFrame(windows, text="Song List", width=250, height=200, bg="pink")
sng_lst.place(x=600, y=0, width=400, height=200)

scrol = Scrollbar(sng_lst, orient=VERTICAL)

playlist = Listbox(sng_lst, yscrollcommand=scrol.set, selectbackground="gold", selectmode=SINGLE, font="bold")

scrol.pack(side=RIGHT, fill=Y)
scrol.config(command=playlist.yview)
playlist.pack(fill=BOTH)

os.chdir('playlist')

songtracks = os.listdir()

for track in songtracks:
    playlist.insert(END, track)


def play():
    #track.set(playlist.get(ACTIVE))

    status.set(playlist.get(ACTIVE))

    pygame.mixer.music.load(playlist.get(ACTIVE))

    pygame.mixer.music.play()

    #songstatus['text'] =


play_btn = Button(cntrl_panel, text="PLAYSONG", command=play, width=10, height=1, bg="white")
play_btn.grid(row=0, column=0, padx=10, pady=5)


def pause():
    status.set("-Paused")
    pygame.mixer.music.pause()


pause_btn = Button(cntrl_panel, text="PAUSE", command=pause, width=8, height=1, bg="white")
pause_btn.grid(row=0, column=1, padx=10, pady=5)


def unpause():
    status.set("-Unpause")
    pygame.mixer.music.unpause()


unpause_btn = Button(cntrl_panel, text="UNPAUSE", command=unpause, width=10, height=1, bg="white")
unpause_btn.grid(row=0, column=2, padx=10, pady=5)


def stop():
    status.set("-Stopped")
    pygame.mixer.music.stop()


stp_btn = Button(cntrl_panel, text="STOPSONG", command=stop, width=10, height=1, bg="white")
stp_btn.grid(row=0, column=3, padx=10, pady=5)

windows.mainloop()
