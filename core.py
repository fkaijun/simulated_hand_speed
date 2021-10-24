from pymouse import PyMouse
import time
from PyQt5.QtCore import QThread


class MyThread(QThread):
    def __init__(self, time_code, pos):
        super(MyThread, self).__init__()
        self.time_code = time_code
        self.pos = pos

    def run(self):
        while True:
            current_time = time.strftime('%H:%M:%S', time.localtime(time.time()))  # get current time
            if self.time_code == current_time:
                mouse = PyMouse()
                mouse.click(*self.pos)
                break
