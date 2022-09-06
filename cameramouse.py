import pyautogui
import cv2
import mediapipe as mp
import time
import math
import numpy as np

import mouse

def multiply_lms(lms):
    return int(lms.x*w),int(lms.y*h)

#landmarks
def get_lms(myHand):
    lms=[4,8,10,11,12,15,16,20]
    landmarks=np.array(myHand.landmark)[lms]
    multiply=np.vectorize(multiply_lms)
    landmarksx,landmarksy=multiply(landmarks)
    landmarks=np.vstack((landmarksx,landmarksy)).T
    return landmarks

def button_events(lengths,lmList,btnHold):
    #left button hold
    if lengths[0]<30 and btnHold==False:
        mouse.press(button='left')
        return True
    elif lengths[0]>30 and btnHold==True:
        mouse.release(button='left')
        return False

    #double click
    elif lengths[4]<20 and lengths[2]<20 and lengths[6]<20:
        mouse.double_click(button='left')
        return False

    #left click
    elif lengths[2]<20:
        mouse.click()
        return False
            
    #right click
    elif lengths[4]<20:
        mouse.right_click()
        return False
    else:
        return btnHold

#movement and scroll
def movement_and_scroll(lengths):
    if lengths[1]<30 and lengths[3]<30 and lengths[5]<30:
        scrll=int(lmList[2][1]-lmList[4][1])
        mouse.wheel(scrll//10)
    elif lengths[1]<30:
        xCoordinate=round(np.interp(lmList[1][0],(roi[0][0],roi[0][1]),(0,sWidth)))
        yCoordinate=round(np.interp(lmList[1][1],(roi[1][0],roi[1][1]),(0,sHeight)))
        mouse.move(xCoordinate,yCoordinate)

sWidth,sHeight=pyautogui.size()
k=sWidth/sHeight
btnHold=False

mp_hands=mp.solutions.hands

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,round(k*cv2.CAP_PROP_FRAME_HEIGHT))

pTime=0
with mp_hands.Hands() as hands:
    while True:
        _,img=cap.read()
        img=cv2.flip(img,1)
        h,w,_=img.shape
        roi=[(w//4,w-w//4),(h//8,h-3*h//8)]

        cv2.rectangle(img,(roi[0][0],roi[1][0]),(roi[0][1],roi[1][1]),(255,0,0),1)

        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=hands.process(imgRGB)
        
        if results.multi_hand_landmarks:

            myHand=results.multi_hand_landmarks[0]

            lmList=get_lms(myHand)

            #lengths between landmarks
            length_10=math.hypot(lmList[1,0]-lmList[0,0],lmList[1,1]-lmList[0,1])
            length_31=math.hypot(lmList[3,0]-lmList[1,0],lmList[3,1]-lmList[1,1])
            length_60=math.hypot(lmList[6,0]-lmList[0,0],lmList[6,1]-lmList[0,1])
            length_63=math.hypot(lmList[6,0]-lmList[3,0],lmList[6,1]-lmList[3,1])
            length_70=math.hypot(lmList[7,0]-lmList[0,0],lmList[7,1]-lmList[0,1])
            length_75=math.hypot(lmList[7,0]-lmList[5,0],lmList[7,1]-lmList[5,1])
            length_76=math.hypot(lmList[7,0]-lmList[6,0],lmList[7,1]-lmList[6,1])
            lengths=[length_10,length_31,length_60,length_63,length_70,length_75,length_76]
            
    
            btnHold=button_events(lengths,lmList,btnHold)
   
            movement_and_scroll(lengths)

        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f"FPS : {int(fps)}",(550,10),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)

        cv2.imshow("Camera",img)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
