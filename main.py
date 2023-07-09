import threading as th
from time import sleep

plist=input('Enter the playlist: ')

videos=list(Playlist(plist))
print(videos)
from yt_dlp import YoutubeDL

with YoutubeDL() as ydl:
    ydl.download(videos)
    
print('----------done---------')