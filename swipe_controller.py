from typing import List

from pyautogui import press, hotkey
from abc import ABC, abstractmethod

class SwipeController:
    def __init__(self, os: str, swipe_type: str):
        self.os: str = os
        self.swipe_type: str = swipe_type

    def swipe_right(self) -> None:
        print("Swipe right")
        SwipeRight(self.os, self.swipe_type).swipe()

    def swipe_left(self) -> None:
        print("Swipe left")
        SwipeLeft(self.os, self.swipe_type).swipe()

    def is_swipe_right(self, left_up_fingers: List[bool]) -> bool:
        return (not left_up_fingers[0] and left_up_fingers[1] and left_up_fingers[2] and
                not left_up_fingers[3] and not left_up_fingers[4])

    def is_swipe_left(self, right_up_fingers: List[bool]) -> bool:
        return (not right_up_fingers[0] and right_up_fingers[1] and right_up_fingers[2] and
                not right_up_fingers[3] and not right_up_fingers[4])


class SwipeAction(ABC):
    def __init__(self, os: str, swipe_type: str):
        self.os = os
        self.swipe_type = swipe_type

    @abstractmethod
    def swipe(self) -> None:
        pass


class SwipeRight(SwipeAction):
    def swipe(self) -> None:
        if self.os == "mac":
            if self.swipe_type == "screens":
                hotkey('ctrl', 'right')
            elif self.swipe_type == "slides":
                hotkey('right')
        elif self.os == "windows":
            if self.swipe_type == "screens":
                press('alt', 'tab')
            elif self.swipe_type == "slides":
                press('right')


class SwipeLeft(SwipeAction):
    def swipe(self) -> None:
        if self.os == "mac":
            if self.swipe_type == "screens":
                hotkey('ctrl', 'left')
            elif self.swipe_type == "slides":
                hotkey('left')
        elif self.os == "windows":
            if self.swipe_type == "screens":
                press('alt', 'shift', 'tab')
            elif self.swipe_type == "slides":
                press('left')
