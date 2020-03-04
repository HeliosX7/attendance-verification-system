#custom face recognition dataset

import numpy as np
import cv2
import os

vid=cv2.VideoCapture(0)

top=0

!mkdir images

p=!pwd
path=p[0]+'/images'

person_name="James Harrison"

while (True):
    
    ret,frame=vid.read()
    
    gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',gframe)
    
    if cv2.waitKey(30) & 0xFF == ord('k'):
        filename=person_name+str(top)+'.jpg'
        top=top+1
        filename=path+'/'+filename
        cv2.imwrite(filename,gframe)
        
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
        
       
vid.release()
cv2.destroyAllWindows()      w
