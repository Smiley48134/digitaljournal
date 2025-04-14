import pickle

class Entry:
    def __init__(self, entrynum=0,entrywords=""):
        self.num=entrynum
        self.words=entrywords

    def __repr__(self):
        return "entry " + str(self.num) + ".\n" + self.words

def enterentry():
    a = int(input())
    b = input()
    c = Entry(a, b)
    return c
