from tkinter import *
import pygame
import os

class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("360x450+800+80")
        self.root.resizable(False, False)
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        f1 = Frame(self.root, bg="#FA7900")
        f1.place(x=0, y=0, width=360, height=70)

        f2 = Frame(self.root, bg="#1A1A1A")
        f2.place(x=0, y=70, width=360, height=380)

        lbl_title= Label(f1,text="Music Player",font=("Fixedsys",26),bg="#FA7900",fg="white").place(x=55,y=10)
        trackframe = LabelFrame(f2, font=("times new roman", 15, "bold"), bg="#1A1A1A", fg="white",bd=1, relief=GROOVE)
        trackframe.place(x=0, y=0, width=360, height=50)

        songtrack = Label(trackframe, textvariable=self.track, width=24, font=("times new roman", 12, "bold"), bg="#1A1A1A",
                          fg="white").grid(row=0,column=0,padx=10,pady=8)

        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 12, "bold"), bg="#1A1A1A",
                            fg="white").grid(row=0,column=1,padx=10,pady=5)

        keyframe = LabelFrame(self.root, text="Controls",font=("times new roman",12,"bold"),bg="#1A1A1A",fg="#FA7900", bd=2, relief=GROOVE)
        keyframe.place(x=0, y=130, width=360, height=100)

        playbtn = Button(keyframe, text="▷",command=self.playsong,  width=4,
                         font=("times new roman", 20, "bold"), fg="white", bg="#1A1A1A").place(x=270,y=15,height=40)
        playbtn = Button(keyframe, text="■",command=self.pausesong,  width=4,
                         font=("times new roman", 20, "bold"), fg="white", bg="#1A1A1A").place(x=100,y=15,height=40)
        playbtn = Button(keyframe, text="▶",command=self.unpausesong, width=4,
                         font=("times new roman", 20, "bold"), fg="white", bg="#1A1A1A").place(x=185,y=15,height=40)
        playbtn = Button(keyframe, text="⨀",command=self.stopsong, width=4,
                         font=("times new roman", 20, "bold"), fg="white", bg="#1A1A1A").place(x=15,y=15,height=40)

        songslist = LabelFrame(f2, text="Playlist", font=("times new roman", 15, "bold"), bg="#1A1A1A",
                                fg="#FA7900", bd=5, relief=GROOVE)
        songslist.place(x=0, y=160, width=360, height=220)

        scrol_y = Scrollbar(songslist, orient=VERTICAL)
        scrol_x = Scrollbar(songslist, orient=HORIZONTAL)

        self.playlist = Listbox(songslist, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, selectbackground="#FA7900", selectmode=SINGLE,
                                font=("verdana", 10, "bold"), bg="#1A1A1A", fg="white", bd=2, relief=GROOVE)

        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_x.config(command=self.playlist.xview)

        self.playlist.pack(fill=BOTH)
        os.chdir("C:/Users/Yaman Goyal/Music/Songs")

        songtracks = os.listdir()

        for track in songtracks:
            self.playlist.insert(END, track)

    #------------Functions------

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set("-Listening")
        pygame.mixer.music.unpause()


root = Tk()
MusicPlayer(root)
root.mainloop()