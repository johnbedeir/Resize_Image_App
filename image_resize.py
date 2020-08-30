from tkinter import *
import glob
import cv2
<<<<<<< HEAD
=======
from math import *
>>>>>>> 37c83a74771a7b7b76ecc06e08be04a958cba23d

window=Tk()
window.title("Images Resize App")

jpg=glob.glob("*.jpg")
png=glob.glob("*.png")
jpeg=glob.glob("*.jpeg")

def resize_jpg():
    for image in jpg:
        img=cv2.imread(image,1)
        resize=cv2.resize(img,(int(e1.get()),int(e2.get())))
        cv2.imwrite("resized"+image, resize)

def resize_jpeg():
    for image in jpeg:
        img=cv2.imread(image,1)
        resize=cv2.resize(img,(int(e1.get()),int(e2.get())))
        cv2.imwrite("resized"+image, resize)

def resize_png():
    for image in png:
        img=cv2.imread(image,1)
        resize=cv2.resize(img,(int(e1.get()),int(e2.get())))
        cv2.imwrite("resized"+image, resize)

#Labels
l1=Label(window, text="Type the resolution")
l1.grid(row=1,column=1)

l1=Label(window, text="X")
l1.grid(row=1,column=3)


#Entries
e1=Entry(window, width=6)
e1.grid(row=1,column=2)

e2=Entry(window, width=6)
e2.grid(row=1,column=4)


#Buttons
b1=Button(window,text="Resize All JPG", width=12, command=resize_jpg)
b1.grid(row=1,column=5)

b2=Button(window,text="Resize All JPEG", width=12, command=resize_jpeg)
b2.grid(row=2,column=5)

b3=Button(window,text="Resize All PNG", width=12, command=resize_png)
b3.grid(row=3,column=5)

window.mainloop()
