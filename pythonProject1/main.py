import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8)
faceRead = FaceDetector(minDetectionCon=0.8)
faceMeshRead = FaceMeshDetector(maxFaces=2)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, _ = detector.findPosition(img)


    #image_data = faceRead.findFaces(img)
    #imageinface = faceMeshRead.findFaceMesh(img)
    #img2 = detector.findDistance(img)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
