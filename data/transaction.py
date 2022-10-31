import json
import time
import hashlib
import _json
class transaction():

    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = time.asctime(time.localtime(time.time()))

    def to_dict(self): #rap up the transaction by a dict
        identity = ""
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender
        return {
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time}

    def show_trans(self):
        print(json.dumps(self.__dict__, sort_keys=True))
