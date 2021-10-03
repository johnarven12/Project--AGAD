import glob
import os

list_of_files = glob.glob('C:/Users/ceejay/Desktop/bssoup/*.mp4*') # * means all if need specific format then *.mp4
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

import moviepy.editor as mp

my_clip = mp.VideoFileClip(r""+latest_file+"")
my_clip.audio.write_audiofile(r"C:/Users/ceejay/Desktop/bssoup/koyakim.wav")
