import numpy as np
import cv2
import os
from Tkinter import *
from random import choice
from string import ascii_uppercase
import copy





cap = cv2.VideoCapture(1)

imgname=''
imgname=imgname.join(choice(ascii_uppercase) for i in range(12))
outputimg = copy.copy(imgname)

imgname = 'inputs/'+imgname+'.jpg'


 
while(True):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
    	cv2.imwrite(imgname,frame)
        break

cap.release()
cv2.destroyAllWindows()

master = Tk()

selected_option = 0
def callback1():
    selected_option = 1
    os.system("python evaluate.py --checkpoint models/la_muse.ckpt --in-path "+imgname+" --out-path outputs/")
    master.destroy()
    
def callback2():
    selected_option = 2
    os.system("python evaluate.py --checkpoint models/rain_princess.ckpt --in-path "+imgname+" --out-path outputs/")
    master.destroy()
    
def callback3():
    selected_option = 3
    print('Callback3')
    os.system("python evaluate.py --checkpoint models/scream.ckpt --in-path "+imgname+" --out-path outputs/")
    master.destroy()
    
def callback4():
    selected_option = 4
    os.system("python evaluate.py --checkpoint models/wreck.ckpt --in-path "+imgname+" --out-path outputs/")
    master.destroy()
    
def callback5():
    selected_option = 5
    os.system("python evaluate.py --checkpoint models/udnie.ckpt --in-path "+imgname+" --out-path outputs/")
    master.destroy()
    
def callback6():
    selected_option = 6
    os.system("python evaluate.py --checkpoint models/wave.ckpt --in-path "+imgname+" --out-path outputs/")
    master.destroy()
def callback7():
    selected_option = 7
    os.system("python evaluate.py --checkpoint newmodels/ --in-path "+imgname+" --out-path outputs/")
    master.destroy()    

 
photo1=PhotoImage(file="examples/style/la_muse.png")
b1 = Button(master,image=photo1, command=callback1)
b1.pack()

photo2=PhotoImage(file="examples/style/rain_princess.png")
b2 = Button(master,image=photo2, command=callback2)
b2.pack()

photo3=PhotoImage(file="examples/style/the_scream.png")
b3 = Button(master,image=photo3, command=callback3)
b3.pack()

photo4=PhotoImage(file="examples/style/the_shipwreck_of_the_minotaur.png")
b4 = Button(master,image=photo4, command=callback4)
b4.pack()

photo5=PhotoImage(file="examples/style/udnie.png")
b5 = Button(master,image=photo5, command=callback5)
b5.pack()

photo6=PhotoImage(file="examples/style/wave.png")
b6 = Button(master,image=photo6, command=callback6)
b6.pack()

photo7=PhotoImage(file="examples/style/starry-nights.png")
b7 = Button(master,image=photo7, command=callback7)
b7.pack()

mainloop()




img=cv2.imread('outputs/'+outputimg+'.jpg')
cv2.imshow('Formed Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
