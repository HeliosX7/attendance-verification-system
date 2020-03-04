import cv2
import urllib.request
from urllib.error import HTTPError
import numpy as np
import os

#say we take the following list of persons present in the vgg_face_dataset file
p_list=['Taylor_Swift','Bear_Grylls','Cillian_Murphy','Aamir_Khan','Harry_Styles']

for person in p_list:
    person_dir='./images/'+person

    if not os.path.exists(person_dir):
        os.makedirs(person_dir)

    f=open('files/'+person+'.txt','r')
    i=0
    for line in f:
        words=line.split(' ')
        try:
            req=urllib.request.urlopen(words[1])
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)
            cv2.imwrite(person_dir+'/'+person+'_'+words[0]+'.jpg',img)
            if i==20:
                break
            print(i)
            i=i+1
        except Exception as e :
            print(str(e)) 
    
    
