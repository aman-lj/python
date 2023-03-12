import sys
import playsound
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
        self.users=[] # list of instances of user class
        self.musics=[] # list of instances of Music
        self.current_user=None
        self.db_path='/home/aman/python/python-group-project/music.csv' # Hardcoded path
    #def load_database()
    #def add_user(self)
    #def add_fav_song(self,user,song)
    #def add_fav_singer(self,user,)
print("hello, world\n")
