import cv2
import glob
import time
import os


images = glob.glob('slideshowimages/*.jpg')
print(images)
while True:
	for a in images:
		print(a)
		img=cv2.imread(a)
		cv2.namedWindow('Image Already Saved', cv2.WND_PROP_FULLSCREEN)
		os.environ['DISPLAY']=':0.0'
		cv2.moveWindow('Image Already Saved',2000,0)
		cv2.setWindowProperty('Image Already Saved', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)                    
		cv2.imshow('Image Already Saved',img)
		cv2.waitKey(2000)