import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
colorR = (255,0,255)

while True:
    Success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    #if len(hands) == 1:
    if len(hands) == 1:
        lmList1 = hands[0]["lmList"]
        length, info, img = detector.findDistance(lmList1[8], lmList1[12], img)
        cursor = lmList1[12]

        if 100 < cursor[0] < 300 and 100 < cursor[1] < 300:
            colorR = (0,255,0)
        else:
            colorR = (255,0,255)

    #elif len(hands) == 2:
      #  print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))

    cv2.rectangle(img, (100,100), (300,300), colorR, cv2.FILLED)
    #img = cv2.flip(img, 1)

    cv2.imshow("Hollow.os", img)
    cv2.waitKey(1)
