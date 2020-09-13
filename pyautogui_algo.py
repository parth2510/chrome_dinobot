#import pyautogui as pg
import time 
import numpy as np
from PIL import ImageGrab , ImageOps


def jump(): ## presses spacebar(for jump) in the keyboard
     pg.keyUp('down') 
     pg.press('space') 
     time.sleep(0.01)
     #pg.keyDown('down')
    
def pixelsum(): # presses down to save from flying dinos
    im1=ImageGrab.grab((677,182,1336-450,298))
    grayim1=ImageOps.grayscale(im1)
    ar=np.array(grayim1.getcolors())
    return ar.sum()
    
    
time.sleep(5)

while True: #-->>>> warning- once the game gets over, quickly move the cursor to any corner to stop the script from running <<<--##

    if pixelsum() > 26971+1700: # the sum 
        jump()
        print('jumped',pixelsum(),end= " ")
        time.sleep(0.05)
        
    elif pixelsum() < 26681+1000:
        pg.keyDown('down')
        #time.sleep(0.01)
#print(pixelsum())
