import cv2
import numpy as np

#import time

# Buka kamera
cap = cv2.VideoCapture(2)
cap1 = cv2.VideoCapture(1)

kamera = 'f'
kamera = 'o'

#serialcomm = serial.Serial('COM17', 9600)
#serialcomm.timeout = 1

def utama():
    global kamera
    ret, img = cap.read()
    img = cv2.resize(img, (640,480))
    #cv2.imshow('original',img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_cyan = np.array ([160,112,134])
    upper_cyan = np.array ([179,255,255])
   # lower_magenta = np.array ([159,138,50])
    #upper_magenta = np.array ([170,255,225])
    edges = cv2.Canny(img, 15, 125)

    #mask = cv2.inRange (hsv, lower_magenta, upper_magenta)
    mask = cv2.inRange (hsv, lower_cyan, upper_cyan)
    
    kernel = np.ones((5,5), np.float32)/255
    #median = cv2.medianBlur(res, 15)
    iterations = 1
    dilation = cv2.dilate(mask, kernel, iterations)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    font=cv2.FONT_HERSHEY_COMPLEX
    contours,_ = cv2.findContours(closing.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours)>0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        #luas = w*h

        center_x = x + w // 2
        center_y = y + h // 2
        #return center_x, center_y
        #x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(img,(center_x,center_y), 5, (0, 0, 255), -1)
        a= ''
        if y > 320:
            if x <160:
                a='a'
                
            elif x < 320:
                a = 'b'
            elif x<480:
                a= 'c'
            else:
                a = 'd'
                #kamera = 'f'
        elif y>160:
            
            if x <160:
                a='e'
                
            elif x < 320:
                a = 'm'
            elif x<480:
                a= 'g'
            else:
                a = 'h'
        
        elif y>=0:
            
            if x <160:
                a='i'
                
            elif x < 320:
                a = 'j'
            elif x<480:
                a= 'k'
            else:
                a = 'l'
        else:
            kamera='o'



            
       # else : 
           # if x < 300 : 
          #      a = 'L'
          #  elif x > 300:
          #      a ='M'
        #else:
         #   if x > 224:
          #      a ='M'
           # elif x<224:
            #    a ='L'
           
        
        #arduinoData.write(a)
        serialcomm.write(a.encode())
        #print(luas)
        print(a)
        #print(x,y)
    else : 
        kamera = 'o'
    cv2.imshow('closing',mask)
    cv2.imshow('result',img)
    

def omni():
    global kamera
    ret, img = cap1.read()
    img = cv2.resize(img, (640,480))
    #cv2.imshow('original',img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #lower_cyan = np.array ([80,68,120])
    #upper_cyan = np.array ([179,255,255])
    lower_magenta = np.array ([173,132,78])
    upper_magenta = np.array ([179,255,255])
    edges = cv2.Canny(img, 15, 125)

    mask = cv2.inRange (hsv, lower_magenta, upper_magenta)
    
    kernel = np.ones((5,5), np.float32)/255
    #median = cv2.medianBlur(res, 15)
    iterations = 1
    dilation = cv2.dilate(mask, kernel, iterations)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    font=cv2.FONT_HERSHEY_COMPLEX
    contours,_ = cv2.findContours(closing.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours)>0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        #luas = w*h

        center_x = x + w // 2
        center_y = y + h // 2
        #return center_x, center_y
        #x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(img,(center_x,center_y), 5, (0, 0, 255), -1)
        a= ''
        if y > 240:
            if x < 320:
                a = 'p'
                kamera = 'f'
            elif x < 640:
                a = 'q'
                kamera = 'f'
            
        elif y>0:
            if x < 320:
                a = 'r'
            elif x < 640:
                a = 's'

            
       # else : 
           # if x < 300 : 
          #      a = 'L'
          #  elif x > 300:
          #      a ='M'
        #else:
         #   if x > 224:
          #      a ='M'
           # elif x<224:
            #    a ='L'
           
        
        #arduinoData.write(a)
        serialcomm.write(a.encode())
        #print(luas)
        print(a)
       # print(x,y)
    else : 
        kamera = 'f'
    cv2.imshow('closing',closing)
    cv2.imshow('resul-1m',img)
    #navigasi = cv2.putText((a), (275, 50), font, 1, (0,0, 255), 2, cv2.LINE_AA)
    #cv2.imshow('arah',(a))
        

while True:
    # Baca frame dari aliran video
    #omni()
    #utama()
    if kamera =='f':
        utama()
    elif kamera =='o':
        omni()
   
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
