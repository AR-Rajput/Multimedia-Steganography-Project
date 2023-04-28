import math
import cv2
import os
from stegano import lsb


def split_string(s_str ,count=17):
    per_c = math.ceil(len(s_str)/count)
    c_cout = 0
    out_str = ''
    split_list = []
    for s in s_str:
        out_str += s
        c_cout += 1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str = ''
            c_cout = 0
    if c_cout != 0:
        split_list.append(out_str)
    return split_list


def encode_string(message ,root="./ImageStegano/InputFrames/"):
    split_string_list = split_string(message)
    for i in range(0, len(split_string_list)):
        f_name="{}frame{}.png".format(root,i)
        secret_enc=lsb.hide(f_name, split_string_list[i])
        secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name, split_string_list[i]))


def frame_extraction(video):
    
    success = 1
    if video.isOpened():
        current_frame = 0
        while success:
            success, frame = video.read()
            if success: 
                cv2.imwrite(f"./ImageStegano/InputFrames/frame{current_frame}.png", frame)
                current_frame += 1
                
    
def main():
    message = input()
    vidcap = cv2.VideoCapture("./ImageStegano/Video/animation-14035.mp4")
    frame_extraction(vidcap)
    encode_string(message)
    


main()




