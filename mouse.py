#!/usr/bin/python
import sys
sys.path.append('./PyUserInput')

from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent
from threading import Thread

m = PyMouse()
k = PyKeyboard()
class ClickJob(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.mouse_click = MouseClick()

    def tap(self, keycode, character, press):
        if character == 's' and press == True and self.mouse_click.isAlive() == False:
            self.mouse_click.start()
            print 'start'
        elif character == 's' and press == True and self.mouse_click.isAlive() == True:
            self.mouse_click.stop()
            self.mouse_click = MouseClick()
            print 'stop'


    def stop(self):
        super(ClickJob, self).stop()
        if (self.mouse_click != None and isinstance(self.mouse_click, MouseClick)):
            self.mouse_click.stop()

class MouseClick(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.state = False

    def run(self):
        self.state = True
        while self.state == True:
            x, y = m.position()
            m.click(x, y, button=1, n=1)
            #print 'Mouse click at ', x, y, '.'

    def stop(self):
        self.state = False


click_job = ClickJob()
click_job.start()
click_job.join()
