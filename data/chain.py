import json
import time
import datetime
from integrity import integrity_check
import block
import flask
from flask import Flask, jsonify, request
from block import Block
from transaction import *


class BLKchain():
    difficulty = 1

    def __init__(self):
        self.lastID = -1
        self.list = []
        self.unconfirmed_trans = []
        self.lasthash = None

    # block( p_hash,lastID, trans)
    # define system, genblock using ID 0, and 0 is also the system user ID
    def add_genblock(self):
        tran = transaction("System", 'None',"None", "gennesis block")
        block = Block(self.lasthash, self.lastID, tran.to_dict())
        self.list.append(block)
        self.lasthash = block.hash
        self.lastID += 1

    # more strict way to add a block, need to proceed validator
    def add_pblock(self, block, hash):
        previous_hash = self.lasthash

        if previous_hash != block.p_hash:
            return False

        if not BLKchain.is_valid_proof(block, hash):
            return False

        block.hash = hash
        self.list.append(block)
        self.lasthash = hash
        self.lastID += 1
        return True

    def add_block(self, trans):
        block = Block(self.lasthash, self.lastID, trans)
        self.list.append(block)
        self.lasthash = block.hash
        self.lastID += 1

    def block_dict(self, block):
        return block.__dict__

    def show(self):
        json_res = json.dumps(self.list, default=self.block_dict)

        print(json_res)
        return json_res

    """
    proof of work coding part. Assome difficulty is 2
    """

    @staticmethod
    def pow(block):

        block.nonce = 0

        computed_hash = block.getHash()
        while not computed_hash.startswith('0' * BLKchain.difficulty):
            block.nonce += 1
            computed_hash = block.getHash()

        return computed_hash

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        return (block_hash.startswith('0' * BLKchain.difficulty) and
                block_hash == block.getHash())

    def addtransaction(self, trans):
        self.unconfirmed_trans.append(trans.to_dict())

    def addtransaction2(self, sender,course, info, data):
        tran = transaction(sender, course,info, data)
        self.unconfirmed_trans.append(tran.to_dict())

    def Validator(self):
        for i in range(1, len(self.list)):
            current = self.list[i]
            previous = self.list[i - 1]
            if current.hash != current.get_hash():
                print("hash value is not equal")
                return False
            if current.p_hash != previous.hash:
                print("previous hash is not equal")
                return False
            print("All blocks are correct")
            return True

    def mine(self):
        """
        dig a new block, implemented pow
        """
        if not self.unconfirmed_trans:
            return False

        new_block = Block(p_hash=self.lasthash,
                          lastID=self.lastID,
                          trans=self.unconfirmed_trans.pop(),  ##
                          )

        proof = self.pow(new_block)
        self.add_pblock(new_block, proof)
        # self.unconfirmed_trans = []
        return True  # return {dig_is_finished : True }

    ################ contract phase ####################################
    ################ contract of chacking and submitting homework#######
def get_time_stamp(valid_time):
    dd = datetime.datetime.strptime(valid_time, '%m/%d/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    ts = int(time.mktime(time.strptime(dd, '%Y-%m-%d %H:%M:%S')))
    return ts

# asctime（year，month，day，clock，min，sec，weekday，which day，summertime?1/0）
class contract1():
    def __init__(self, name, dtime):
        self.chain = BLKchain()
        self.chain.add_genblock()
        self.instructor_name = name
        self.deadline = dtime

    def copy_check(self, data1, data2):
        i = integrity_check(data1, data2)
        if i > 66:
            return True
        else:
            return False

    def upload_hw(self, sender, course, data):
        #now = time.asctime(time.localtime(time.time()))
        now = time.time()
        dead = get_time_stamp(self.deadline)

        if now > dead:
            print("homework submit is late")
            return "Homeworklate"
        for i in range(1, len(self.chain.list)):
            check = self.copy_check(data, self.chain.list[i].trans['data'])
            if check:
                print("homework is too similar to the others")
                return "HomeworkCheat"
        self.chain.addtransaction2(sender, course, 'checked', data)
        self.chain.mine()
        return "OK"

    def check_all_hw(self):
        l=[]
        for i in range(1,len(self.chain.list)):
            l.append([self.chain.list[i].trans['sender'],self.chain.list[i].trans['course'],self.chain.list[i].trans['data']])
        print(l)
        return l



class contract2():
    def __init__(self):
        self.chain = BLKchain()
        self.chain.add_genblock()

    def register(self, name, course):
        reg = register(name, course, 'reg')
        self.chain.addtransaction(reg)
        self.chain.mine()
        

    def drop(self, name, course):
        reg = register(name, course, 'drop')
        self.chain.addtransaction(reg)
        self.chain.mine()

    def showlist(self):
        l = []
        for i in range(1, len(self.chain.list)):
            if self.chain.list[i].trans['status'] == 'reg':
                if [self.chain.list[i].trans['student name'],self.chain.list[i].trans['course']] not in l:
                    l.append([self.chain.list[i].trans['student name'],self.chain.list[i].trans['course']])
            elif self.chain.list[i].trans['status'] == 'drop':
                try:
                    l.remove([self.chain.list[i].trans['student name'],self.chain.list[i].trans['course']])
                except:
                    pass
        return l

    def search(self,name):
        l = self.showlist()
        l2 = []
        for i in range(1, len(l)):
            if l[i][0]==name:
                l2.append(l[i])
        return l2

    ################ contract phase end ################################

# b = Block(0,"HQ27716",[])
# contract = contract1('Tom', time.asctime((2022, 11, 16, 5, 6, 6, 0, 0, 0)))
# s1 = open('h.txt', 'r').read()
# contract.upload_hw("Haowei5596", s1)
# contract.chain.show()

# chain1 = BLKchain()
# chain1.add_genblock()
# asctime（year，month，day，clock，min，sec，weekday，which day，summertime?1/0）
# time1 = time.asctime((2022, 11, 14, 5, 6, 6, 0, 0, 0))
# time2 = time.asctime((2021, 11, 14, 5, 6, 6, 0, 0, 0))
# print()
# chain1.add_block(chain1.lasthash, "HQ265512", [])
# chain1.addtransaction2("HQ265512","HY883113",5)
# chain1.addtransaction2("HQ265512", open('h.txt', 'r').read(), "passed")
# print(chain1.unconfirmed_trans)
# chain1.mine()
# chain1.show()

# contract = contract1('Tom', time.asctime((2022, 11, 29, 5, 6, 6, 0, 0, 0)))
# s1 = open('h.txt', 'r').read()
# print(integrity_check(s1, s1))
# contract.upload_hw("Haowei5596", 'ICSI210', s1)
# contract.upload_hw("Haowei5596", 'ICSI210', s1)
# contract.chain.show()
# contract.check_all_hw()