from time import sleep
from sys import exit
from playsound import playsound
from win32api import GetAsyncKeyState


class Ikun():
    def j(self):
        playsound(r"sounds/j.mp3", block=False)


    def ni_gan_ma(self):
        playsound(r"sounds/ngm.mp3",block=False)

    def n(self):
        playsound(r"sounds/n.mp3", block=False)

    def t(self):
        playsound(r"sounds/t.mp3", block=False)

    def m(self):
        playsound(r"sounds/m.mp3", block=False)

    def keyboard_listener(slef,key):
        sleep(0.01)
        if GetAsyncKeyState(key):
            return True

    def main_loop(self):
        while not GetAsyncKeyState(0x21):
            if self.keyboard_listener(0x4a) and not self.keyboard_listener(0X11):
                self.j()
            elif self.keyboard_listener(0x4e):
                self.n()
            elif self.keyboard_listener(0x54):
                self.t()
            elif self.keyboard_listener(0x4d):
                self.m()
            elif GetAsyncKeyState(0x11) and GetAsyncKeyState(0x4a):
                self.ni_gan_ma()


a = Ikun()
a.main_loop()
exit()

