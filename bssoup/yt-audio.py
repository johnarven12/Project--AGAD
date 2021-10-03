
#import the package
from pytube import YouTube
url = 'https://www.youtube.com/watch?v=59JeDyt9UjU'
print(url)
my_video = YouTube(url)
print("*********************Video Title************************")
#get Video Title
print(my_video.title)

print("********************Thumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("********************Download video*************************")
#get all the stream resolution for the
for stream in my_video.streams:
    print(stream)
#set stream resolution
my_video = my_video.streams.get_highest_resolution()
#my_video = my_video.streams.first()
#Download video
my_video.download()

#get the latest file in the download folder
import glob
import os
list_of_files = glob.glob('C:/Users/ceejay/Desktop/bssoup/*.mp4*') # * means all if need specific format then *.mp4
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

#convert it to .wav format
import moviepy.editor as mp
my_clip = mp.VideoFileClip(r""+latest_file+"")
my_clip.audio.write_audiofile(r"C:/Users/ceejay/Desktop/bssoup/data1.wav")


#audio conversion py
from os import path
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('C:/Users/ceejay/Desktop/bssoup/data1.wav') as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('working on...')
            #print(text)
            f = open("C:/Users/ceejay/Desktop/bssoup/demofile.txt", "a")
            f.write(text)
            f.close()
            #open and read the file after the appending:
            f = open("C:/Users/ceejay/Desktop/bssoup/demofile.txt", "r")
            print(f.read())
        except:
            print('sorry... run again..')
