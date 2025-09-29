import cv2
import mediapipe as mp
import time
import cv2
import mediapipe as mp



cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()    
mpdraw = mp.solutions.drawing_utils
ptime = 0
ctime =0
while True:
    suceess , img = cap.read()
    imagrRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

    results = hands.process(imagrRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id ,  lm in enumerate(handLms.landmark):
                print(id , lm)
                h , w , c = img.shape
                cx, cy =int(lm.x*w) , int(lm.y*h)
                print(id ,cx , cy)
            mpdraw.draw_landmarks(img , handLms , mpHands.HAND_CONNECTIONS)
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img ,str(int(fps)) ,(10,70) , cv2.FONT_HERSHEY_COMPLEX ,3 , (255,0,255) ,3)
    cv2.imshow('iamges',img)
    cv2.waitKey(1)
    

    




