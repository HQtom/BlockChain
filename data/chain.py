import json
import block
import flask
from flask import Flask, jsonify, request
from block import Block
from transaction import transaction
class BLKchain():

    difficulty = 1

    def __init__(self):
        self.lastID=-1
        self.list = []
        self.unconfirmed_trans=[]
        self.lasthash = None

#block( p_hash,lastID, trans)
#define system, genblock using ID 0, and 0 is also the system user ID
    def add_genblock(self):
        tran = transaction("","",0)
        block = Block(self.lasthash, self.lastID, tran.to_dict())
        self.list.append(block)
        self.lasthash = block.hash
        self.lastID +=1

# more strict way to add a block, need to proceed validator
    def add_pblock(self,block,hash):
        previous_hash = self.lasthash

        if previous_hash != block.p_hash:
            return False

        if not BLKchain.is_valid_proof(block, hash):
            return False

        block.hash = hash
        self.list.append(block)
        self.lasthash = hash
        self.lastID+=1
        return True

    def add_block(self,trans):
        block = Block(self.lasthash,self.lastID, trans)
        self.list.append(block)
        self.lasthash = block.hash
        self.lastID +=1


    def block_dict(self,block):
        return block.__dict__
    def show(self):
        json_res = json.dumps(self.list, default=self.block_dict)
        print(json_res)

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

    def addtransaction2(self,sender,receiver,amount):
        tran = transaction(sender,receiver,amount)
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
                          trans=self.unconfirmed_trans,
                          )

        proof = self.pow(new_block)
        self.add_pblock(new_block, proof)
        self.unconfirmed_trans= []
        return True #return {dig_is_finished : True }

#b = Block(0,"HQ27716",[])
#chain1 = BLKchain()
#chain1.add_genblock()
#chain1.add_block(chain1.lasthash, "HQ265512", [])
#chain1.addtransaction2("HQ265512","HY883113",5)
#chain1.addtransaction2("HQ265512","HY883113",5)
#print(chain1.unconfirmed_trans)
#chain1.mine()
#chain1.show()


