import os
import cv2

data = cv2.VideoCapture("D:/Python/Pycharm/Project/Minor-Project/ImageStegano/Video/animation-14035.mp4")
fps = data.get(cv2.CAP_PROP_FPS)

image_path = "D:/Python/Pycharm/Project/Minor-Project/ImageStegano/InputFrames/"
images = os.listdir(image_path)

image_list = []
count = 0

for i in images: 

    k = "D:/Python/Pycharm/Project/Minor-Project/ImageStegano/InputFrames/frame%s.png" % count
    image_list.append(k)
    count = count + 1
    # print(k)


fourcc = cv2.VideoWriter_fourcc(*'mp4v') #encoding algorithm
frame = cv2.imread(image_list[0])
frame_size = list(frame.shape)
del frame_size[2]
frame_size.reverse()

video = cv2.VideoWriter("D:/Python/Pycharm/Project/Minor-Project/ImageStegano/output_video.mp4", fourcc, fps, frame_size)

for i in range(len(images)):
    video.write(cv2.imread(image_list[i]))
    # print("frame", i+1,)

video.release()