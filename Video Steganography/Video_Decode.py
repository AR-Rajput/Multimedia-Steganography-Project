import cv2
import os
from stegano import lsb

def frame_extraction(video):
    success = 1
    if video.isOpened():
        current_frame = 0
        while success:
            success, frame = video.read()
            if success: 
                cv2.imwrite(f"./ImageStegano/OutputFrames/frame{current_frame}.png", frame)
                current_frame += 1

def decode_string(video):
    frame_extraction(video)
    secret=[]
    path="D:/Python/Pycharm/Project/Minor-Project/ImageStegano/OutputFrames/"
    for i in range(len(os.listdir(path))):
        f_name="{}frame{}.png".format(path,i)
        print(f_name)
        secret_dec = lsb.reveal(f_name)
#         if secret_dec == None:
#             break
#         secret.append(secret_dec)
        
#     print(''.join([i for i in secret]))


vidcap = cv2.VideoCapture("D:/Python/Pycharm/Project/Minor-Project/ImageStegano/Videooutput_video.mp4")
decode_string(vidcap)