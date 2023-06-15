# importing the module
from pytube import YouTube
import pandas as pd
import numpy as np


test_txt = "../Dataset/ava_v2.2/ava_train_v2.2.csv"
 
# using loadtxt() get all contents of train csv into numpy array
train_image_data = np.loadtxt(test_txt,delimiter=",", dtype=str)

#open train csv
file = open(test_txt)
videos_list = []
for record in file:
    record = record.split(",")
    video_id = record[0]
    if video_id not in videos_list:
        videos_list.append(video_id)
# print(len(videos_list))
# print(videos_list)
i = 1
f = open("failure.txt", "a")
fs = open("success.txt", "a")
fa = open("all.txt", "a")
for video_id in videos_list:
    # where to save
    SAVE_PATH = "C:/UB/Summer_2023/DL/Codebase/group-12-deep-learning-final-project/Dataset/AVA_videos/train" #to_do
    # link of the video to be downloaded
    link="https://www.youtube.com/watch?v="+video_id
    fa.write(video_id + "\n")

    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    except:
        print("Connection Error") #to handle exception
    try:
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path = SAVE_PATH, filename = video_id + ".mp4")
        print("downloaded video", i , " : ", video_id)
        fs.write(video_id + "\n")
    except Exception as e:
        f.write(video_id+ "\n")
        print(e)
    i += 1
f.close()
fs.close()
fa.close()



