import json
import time
import hashlib
import _json
class transaction():

    def __init__(self, sender, info, data):
        self.sender = sender
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
            'info': self.info,
            'data': self.data,
            'time': self.time}

    def show_trans(self):
        print(json.dumps(self.__dict__, sort_keys=True))
