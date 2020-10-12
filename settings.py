from random import *
import time


class Settings:
    def __init__(self):
        pass

    def get_url(self):
        return "https://www.instagram.com/"

    def random_paus_interval(self, a: int, b: int, log):
        sec = randint(a, b)
        print(log, " wait  => ", sec, "sec")
        time.sleep(sec)
