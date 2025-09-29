import mediapipe as mp
import cv2 
import time 
cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
while True:
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
           mpdraw.draw_landmarks(img , handLms ,mphands.HAND_CONNECTIONS)

    cv2.imshow("images" , img)
    cv2.waitKey(1)