import sys
import os
import json
import playsound
import tkinter as tk
import time
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
    
    def test(self,y):
        print(y)
        #playsound.playsound('/home/aman/Music/Khaab.mp3')


    def homepage(self):
        self.frame = tk.Frame(self.root_win,height=500,width=500,bg='green').grid(row=0,column=0)
        self.image = tk.PhotoImage(file="/home/aman/wallpapers/solids/gray.png")
        self.Button = tk.Button(self.frame,image=self.image,height=400,width=400,command=self.test(3)).grid(row=0,column=0)    
    def submit(self):
        playsound.playsound('/home/aman/Music/nya-3-2.mp3')
#        if self.data[self.username]
        self.frame.destroy()
        self.homepage()
    def login(self):
        self.root_win = tk.Tk()
        self.frame = tk.Frame(self.root_win)
        tk.Label(self.frame, text="Login page", font=('JetBrains Mono', 40, 'bold'), pady=25).grid(row=0, column=0)
        tk.Label(self.frame, text="Username",font=('JetBrains Mono', 20, 'bold'), pady=25, padx=20).grid(row=1, column=6)
        self.username = tk.Entry(self.frame, font=('JetBrains Mono', 20, 'bold')).grid(row=1, column=7)
        tk.Label(self.frame, text="Password",font=('JetBrains Mono', 20, 'bold'), pady=25, padx=20).grid(row=2, column=6)
        self.password = tk.Entry(self.frame, font=('JetBrains Mono', 20, 'bold'), show='*').grid(row=2, column=7)
        tk.Button(self.frame, command=self.submit, text="fuck this").grid(row=3, column=7)
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
