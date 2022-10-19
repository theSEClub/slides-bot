from datetime import datetime

import cv2
from cvzone.HandTrackingModule import HandDetector
import Click

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.5, maxHands=2)
# color = (255, 0, 255)
# cx, cy, w, h = 100, 100, 200, 200
waitingSeconds = 1

waitingSeconds = waitingSeconds * 1000
handTypes = {}
lastAction = datetime.now()
checkRightCounter = 0
checkLeftCounter = 0
lastCheckRight = datetime.now()
lastCheckLeft = datetime.now()

print(lastAction)

while True:
    # print('Reading')
    _, img = cap.read()
    hands, img = detector.findHands(img)
    # hands, img = detector.findHands(img, flipType=False)
    # hands = detector.findHands(img, draw=False)

    # cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), color, cv2.FILLED)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # list of 21 landmarks points
        bbox1 = hand1["bbox"]  # x, y, w, h
        centerPoint1 = hand1["center"]  # cx, cy
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        index_finger1 = lmList1[8]
        middle_finger1 = lmList1[12]

        # cv2.circle(img, index_finger1, 10, color, cv2.FILLED)
        handTypes[handType1] = hand1

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # list of 21 landmarks points
            bbox2 = hand2["bbox"]  # x, y, w, h
            centerPoint2 = hand2["center"]  # cx, cy
            handType2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            handTypes[handType2] = hand2
            rightHand = handTypes.get("Right", 0)
            leftHand = handTypes.get("Left", 0)
            if not rightHand or not leftHand:
                continue
            rightUpFingers = detector.fingersUp(rightHand)
            leftUpFingers = detector.fingersUp(leftHand)
            index_finger2 = lmList2[8]
            middle_finger2 = lmList2[12]
            if not leftUpFingers[0] and leftUpFingers[1] and leftUpFingers[2] and not leftUpFingers[3] and not leftUpFingers[4]:
                index_finger1 = index_finger1[:2]
                index_finger2 = index_finger2[:2]
                length, info, img = detector.findDistance(index_finger1, index_finger2, img)
                # length, info = detector.findDistance(index_finger1, index_finger2)
                if length > 100:
                    now = datetime.now()
                    if (now - lastAction).seconds*1000 > waitingSeconds:
                        lastAction = now
                        print("Right")
                        Click.swipe_right()

            if not rightUpFingers[0] and rightUpFingers[1] and rightUpFingers[2] and not rightUpFingers[3] and not \
            rightUpFingers[4]:
                index_finger1 = index_finger1[:2]
                index_finger2 = index_finger2[:2]
                length, info, img = detector.findDistance(index_finger1, index_finger2, img)
                if length > 100:
                    now = datetime.now()
                    if (now - lastAction).seconds*1000 > waitingSeconds:
                        checkLeftCounter += 1
                        if (now - lastCheckLeft).seconds < 1:
                            lastCheckLeft = now
                            checkLeftCounter = 0

                        if checkLeftCounter > 10:
                            lastAction = now
                            print("Left")
                            Click.swipe_left()
                            checkLeftCounter = 0




    img = cv2.flip(img, 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)