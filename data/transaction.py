import json
import time
import hashlib
import _json

#Transaction structure mainly for online homework adjustment and submittion
class transaction():

    def __init__(self, sender,course, info, data):
        self.sender = sender
        self.course = course
        self.info = info
        self.data = data
        self.time = time.asctime(time.localtime(time.time()))

    def to_dict(self): #rap up the transaction by a dict
        identity = ""
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender
        return {
            'sender': identity,
            'course': self.course,
            'info': self.info,
            'data': self.data,
            'time': self.time}

    def show_trans(self):
        print(json.dumps(self.__dict__, sort_keys=True))


#transaction mainly for the course register
class register():
    def __init__(self, name, course,type):
        self.name = name
        self.course = course
        self.time = time.asctime(time.localtime(time.time()))
        self.type = type

    def to_dict(self): #rap up the transaction by a dict
        identity = ""
        if self.name == "Genesis":
            identity = "Genesis"
        else:
            identity = self.name
        return {
            'student name': identity,
            'course': self.course,
            'registered time': self.time,
            'status':self.type}

    def show_trans(self):
        print(json.dumps(self.__dict__, sort_keys=True))