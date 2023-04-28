from stepic import encode 
from eyed3 import load
from PIL import Image

print(" ###################################### ")

data = str(input("Your Data: "))

audio = input("Audio: ")
img_name = input("IMAGE: ")
audio = load(audio)

img = Image.open(img_name)
img_stegano = encode(img, data.encode())
img_stegano.save(img_name)

audio.initTag()
audio.tag.images.set(3, open(img_name,"rb").read(), "image/png")
audio.tag.save()

print(" ###################################### ")

input(" COMPLETE(press enter to -> exit) ")