from datetime import datetime
from typing import List, Dict, Any

import cv2
from cvzone.HandTrackingModule import HandDetector
from swipe_controller import SwipeController
from time import sleep

class Main:
    def __init__(self):
        os: str = input("What operating system are you using? (mac/windows): ").lower()
        swipe_type: str = input("What do you want to swipe? (screens/slides): ").lower()
        if os not in ("mac", "windows") or swipe_type not in ("screens", "slides"):
            raise Exception("Invalid input")
        print("Initializing software...")

        self.cap: cv2.VideoCapture = cv2.VideoCapture(0)
        self.detector: HandDetector = HandDetector(detectionCon=0.5, maxHands=2)
        self.waiting_seconds: int = 1 * 1000
        self.hand_types: Dict[str, Any] = {}
        self.last_action: datetime = datetime.now()
        self.check_right_counter: int = 0
        self.check_left_counter: int = 0
        self.last_check_right: datetime = datetime.now()
        self.last_check_left: datetime = datetime.now()
        self.swipe_controller: SwipeController = SwipeController(os, swipe_type)

    def run(self) -> None:
        while True:
            _, img = self.cap.read()
            hands, img = self.detector.findHands(img)
            self.process_hands(hands, img)

    def process_hands(self, hands: List[Any], img: cv2.Mat) -> None:
        if hands:
            self.process_single_hand(hands)
            if len(hands) == 2:
                self.process_two_hands(hands, img)

        img = cv2.flip(img, 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

    def process_single_hand(self, hands: List[Any]) -> None:
        hand1 = hands[0]
        hand_type1 = hand1["type"]
        self.hand_types[hand_type1] = hand1

    def process_two_hands(self, hands: List[Any], img: cv2.Mat) -> None:
        hand2 = hands[1]
        hand_type2 = hand2["type"]
        self.hand_types[hand_type2] = hand2
        right_hand = self.hand_types.get("Right", 0)
        left_hand = self.hand_types.get("Left", 0)

        if not right_hand or not left_hand:
            return None

        left_up_fingers = self.detector.fingersUp(left_hand)
        right_up_fingers = self.detector.fingersUp(right_hand)
        lm_list1 = left_hand["lmList"]
        lm_list2 = right_hand["lmList"]
        index_finger1 = lm_list1[8][:2]
        index_finger2 = lm_list2[8][:2]

        length, info, img = self.detector.findDistance(index_finger1, index_finger2, img)
        self._set_last_action(length, index_finger1, index_finger2)

        if self.swipe_controller.is_swipe_right(left_up_fingers):
            self.swipe_controller.swipe_right()
            sleep(0.5)

        if self.swipe_controller.is_swipe_left(right_up_fingers):
            self.swipe_controller.swipe_left()
            sleep(0.5)

    def _set_last_action(self, length: float, index_finger1: List[int], index_finger2: List[int]) -> None:
        if length > 100:
            now = datetime.now()
            if (now - self.last_action).seconds * 1000 > self.waiting_seconds:
                self.last_action = now

if __name__ == "__main__":
    main = Main()
    main.run()