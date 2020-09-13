import pyautogui as pg
import time 
import numpy as np
import pyautogui_algo
from PIL import ImageGrab , ImageOps


i=0 # runs for 5 sec 

# you've to know the coordinates of the dino game in your screen
# the top left corner of the screen is origin with horizontal axis x( left to right) and vertical axis y (top to down)


# hit and try to get the approximate coordinates, can view the image from line 25 aswell

x1= 677 #coordinates of the ingame screen (for me)
y1=182
x2=886 //1336-450
y2=298

# hit and try to get the approximate coordinates, can view the image from line 25 aswell
while True:
    
    im1=ImageGrab.grab((x1,y1,x2,y2)) 
    grayim1=ImageOps.grayscale(im1) # convert image to grayscale
    ar=np.array(grayim1.getcolors()  ) 
    print(ar.sum(),end=' ')  # sum of pixels within the coordinates
    im1.show()      # shows the content of screen within the coordinates ,comment out if want to know just the sum
    time.sleep(1)
    #print(i)
    i=i+1
    if i>5: break
# once you get to know the initial sum of pixels, you can store that to be used in pyautogui_algo 
