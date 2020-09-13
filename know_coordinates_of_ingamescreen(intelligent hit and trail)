i=0 # runs for 5 sec 
x1= 677 #coordinates of the ingame screen 
y1=182
x2=886 //1336-450
y2=298

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
