import sys
import os
import json
import playsound
import tkinter as tk
import time
import multiprocessing
# playsound is library to play a sound independent of platform
# playsound.playsound('path_to_music')
# import tkinter
import sqlite3 # for database

# Example
# playsound.playsound('/home/aman/Music/Khaab.mp3')

class Music:
    # Contains metadata of Music. ie, when it's added, singer name etc.
    def __init__(self, name, singer, genre, music_path):
        self.name=name
        self.singer=singer
        self.path=music_path
        self.genre=genre
        self.play_count=0
    def play(self):
        playsound.playsound(self.path)
class User:
    # It has user's data like username, password, favourite musics.
    def __init__(self, username, passwd):
        self.username=username
        self.passwd=passwd
        self.fav_song=[] # list of name of favourite music
        self.fav_singers=[] # list of name of favourite singers
#

class Frames:
    music = ['/home/kaif/Desktop/python/python-group-project/Music/Deewana Kar Raha Hai - Raaz 3 320 Kbps.mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Coolio - Gangsta\'s Paradise (feat. L.V.) [Official Music Video] [fPO76Jlnz6c].mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Hale Dil - Muder 2 320Kbps.mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Hensonn-Sahara_pIZ0QRWK0zg.mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Hum+Yaar+Hain+Tumhare+Slowed+Reverb+_90s+Lofi+Alka+Yagnik+Udit+Narayan+Use+Headphones+🎧].mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Imagine-Dragons-Bones-Official.mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Ishq Ka Raja - Addy Nagar.mp3',
             '/home/kaif/Desktop/python/python-group-project/Music/Khaab.mp3'
            ]
    thread = 0
    value = 'stop'
    number = 0
    def __init__(self,root_win,number,r,c):
        self.root_win = root_win
        self.r = r 
        # self.thread = 0
        self.number = number
        self.c = c
        self.image = tk.PhotoImage(file="/home/kaif/Desktop/python/index.png")
        self.ipath = tk.PhotoImage(file='play(2).png')
        self.pmusic()

    def add(self):
        self.frame = tk.Frame(self.root_win,height=250,width=250).grid(row=self.r,rowspan=3,column=self.c)

        self.frame1 = tk.Frame(self.frame,height=50,width=250,bg='red').grid(row=self.r,column=self.c)
        if(self.r>=8):
            self.label = tk.Label(self.frame1,text='ARTIST NAME',bg='#004445').grid(row=self.r,column=self.c)
        else:
            self.label = tk.Label(self.frame1,text='SONG NAME',bg='#004445').grid(row=self.r,column=self.c)

        self.frame2 = tk.Frame(self.frame,height=150,width=250,bg='blue').grid(row=self.r+1,column=self.c)
        self.Button = tk.Button(self.frame2,command=self.test,image=self.image,height=150,width=250).grid(row=self.r+1,column=self.c)

        self.frame3 = tk.Frame(self.frame,height=50,width=250,bg='red').grid(row=self.r+2,column=self.c)
        if(self.r>=8):
            self.button = tk.Button(self.frame3,command=self.test,bg='#004445',text='play album').grid(row=self.r+2,column=self.c)
        else:
            self.button = tk.Button(self.frame3,command=self.test,bg='#004445',image=self.ipath).grid(row=self.r+2,column=self.c)
    
    def state(self):
        playsound.playsound(Frames.music[self.number-1])

    def test(self):
        if Frames.number == 0:
            Frames.number = self.number
        if Frames.value == 'stop' and Frames.number == self.number:
            Frames.value = 'start'
            Frames.thread = multiprocessing.Process(target=self.state)
            Frames.thread.start()
        elif Frames.value == 'start' and Frames.number == self.number:
            Frames.value = 'stop'
            Frames.number = 0
            Frames.thread.terminate()
        elif Frames.value == 'start' and Frames.number != self.number:
            Frames.thread.terminate()
            Frames.number = self.number
            Frames.thread = multiprocessing.Process(target=self.state)
            Frames.thread.start()

    def pmusic(self):
        self.label1 = tk.Label(self.root_win, text="play music", font=('JetBrains Mono', 40, 'bold')).grid(row=0,column=5,columnspan=9)
        self.frame1 = tk.Frame(self.root_win,height=100,width=200,bg='#004445').grid(row=1,rowspan=3,column=5)
        self.frame1 = tk.Frame(self.root_win,height=930,width=500,bg='blue').grid(row=1,rowspan=11,column=6,columnspan=3)
        
        self.framep1 = tk.Frame(self.frame1,height=300,width=400,bg='black').grid(row=1,rowspan=4,column=6,columnspan=3)
        self.labelp = tk.Label(self.framep1,height=300,width=400,image=self.image).grid(row=1,rowspan=4,column=6,columnspan=3)
        
        self.framep2 = tk.Frame(self.frame1,height=50,width=400,bg='black').grid(row=5,column=6,columnspan=3)
        self.buttonp = tk.Button(self.framep2,height=50,width=400,image=self.ipath).grid(row=5,column=6,columnspan=3)

        self.framep3 = tk.Frame(self.frame1,height=450,width=400,bg='black').grid(row=6,rowspan=6,column=6,columnspan=3)
        demo = 'this is demo \n this is demo \n this is demo \n this is demo \n'
        self.labelp2 = tk.Label(self.framep3,text=demo).grid(row=6,rowspan=6,column=6,columnspan=3)
        
#
class App:
    # Main application class
    def __init__(self):
        self.users=[] # list of instances of User class
        self.musics=[] # list of instances of Music class
        self.current_user=None
        self.project_dir=os.path.dirname(__file__)
        self.init()
        print("app created succesfully")
    def init(self):
        self.load_data()
        self.login()
    
    def homepage(self):
        tk.Label(self.root_win,bg='#004445', text="music", font=('JetBrains Mono', 40, 'bold'), pady=10).grid(row=0, columnspan=4)
        
        # self.frame = tk.Frame(self.root_win,height=250,width=250,bg='blue').grid(row=1,column=0)
        self.image = tk.PhotoImage(file="/home/kaif/Desktop/python/index.png")
        # self.Button = tk.Button(self.frame,command=self.test,image=self.image,height=200,width=200).grid(row=1,column=0)
        
        self.frame1 = Frames(self.root_win,1,1,0)
        self.frame1.add()
        self.frame2 = Frames(self.root_win,2,1,1)
        self.frame2.add()
        self.frame3 = Frames(self.root_win,3,1,2)
        self.frame3.add()
        self.frame4 = Frames(self.root_win,4,1,3)
        self.frame4.add()

        tk.Label(self.root_win,bg='#004445', text="fav music", font=('JetBrains Mono', 40, 'bold'), pady=10).grid(row=4,columnspan=4)


        self.frame5 = Frames(self.root_win,5,5,0)
        self.frame5.add()
        self.frame6 = Frames(self.root_win,6,5,1)
        self.frame6.add()
        self.frame7 = Frames(self.root_win,7,5,2)
        self.frame7.add()
        self.frame8 = Frames(self.root_win,8,5,3)
        self.frame8.add()


        tk.Label(self.root_win,bg='#004445', text="artist", font=('JetBrains Mono', 40, 'bold'), pady=10).grid(row=8,columnspan=4)


        self.frame9 = Frames(self.root_win,9,9,0)
        self.frame9.add()
        self.frame10 = Frames(self.root_win,10,9,1)
        self.frame10.add()
        self.frame11 = Frames(self.root_win,11,9,2)
        self.frame11.add()
        self.frame12 = Frames(self.root_win,12,9,3)
        self.frame12.add()
      
    def submit(self):
        #playsound.playsound('/home/aman/Music/nya-3-2.mp3')
#        if self.data[self.username]
        print("login page destroyed")
        self.frame.destroy()
        self.homepage()
    def login(self):
        self.root_win = tk.Tk()
        self.root_win.geometry('1700x1200')
        self.root_win.configure(bg='#004445')
        self.frame = tk.Frame(self.root_win)
        tk.Label(self.frame, text="Login page", font=('JetBrains Mono', 40, 'bold'), pady=25).grid(row=0, column=0)
        tk.Label(self.frame, text="Username",font=('JetBrains Mono', 20, 'bold'), pady=25, padx=20).grid(row=1, column=6)
        self.username = tk.Entry(self.frame, font=('JetBrains Mono', 20, 'bold')).grid(row=1, column=7)
        tk.Label(self.frame, text="Password",font=('JetBrains Mono', 20, 'bold'), pady=25, padx=20).grid(row=2, column=6)
        self.password = tk.Entry(self.frame, font=('JetBrains Mono', 20, 'bold'), show='*').grid(row=2, column=7)
        tk.Button(self.frame, command=self.submit, text="submit").grid(row=3, column=7)
        self.frame.pack()
    def load_data(self):
        file=open(f'{self.project_dir}/data.json', 'r')
        self.data=json.loads(file.read())
        file.close()
        print(self.data['users']['aman']['fav_song'])
        self.data['users']['sujal'] = dict()
        file=open(f'{self.project_dir}/data.json', 'w')
        file.write(json.dumps(self.data))
        file.close()
    #def load_database()
    def add_user(self):
        pass
    #def add_fav_song(self,user,song)
    #def add_fav_singer(self,user,)
print("hello, world\n")
print("The project folder is", os.getcwd())
app = App()
app.root_win.mainloop()
