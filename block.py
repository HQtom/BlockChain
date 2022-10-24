import json
import time
import hashlib
import _json


class Block():
    def __init__(self, p_hash, ID, trans):
        self.t_stamp = time.asctime(time.localtime(time.time()))
        self.p_hash = p_hash
        self.ID = ID
        self.trans = trans
        self.hash = self.getHash()
        self.nonce = 0

    def getHash(self):
        #data = self.t_stamp + self.ID + self.p_hash+self.trans
        data = json.dumps(self.__dict__, sort_keys=True)
        hash = hashlib.sha256()
        hash.update(data.encode("ascii"))
        return hash.hexdigest()


