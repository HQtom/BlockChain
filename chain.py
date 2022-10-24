import json
import block
import flask
from block import Block

class BLKchain():

    difficulty = 1

    def __init__(self):
        self.list = []
        self.unconfirmed_trans=[]
        self.lasthash = None

    def add_genblock(self):
        block = Block(0, 0, [])
        self.list.append(block)
        self.lasthash = block.hash

    def add_pblock(self,block,hash):
        previous_hash = self.lasthash

        if previous_hash != block.p_hash:
            return False

        if not BLKchain.is_valid_proof(block, hash):
            return False

        block.hash = hash
        self.list.append(block)
        self.lasthash = hash
        return True

    def add_block(self,ID, name, phash):
        block = Block(phash, ID, name)
        self.list.append(block)
        self.lasthash = block.hash
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
        self.unconfirmed_trans.append(trans)


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

    def mine(self,ID):
        """
        dig a new block, implemented pow
        """
        if not self.unconfirmed_trans:
            return False

        new_block = Block(p_hash=self.lasthash,
                          ID=ID,
                          trans=self.unconfirmed_trans,
                          )

        proof = self.pow(new_block)
        self.add_pblock(new_block, proof)
        self.unconfirmed_trans= []
        return True #return {dig_is_finished : True }

#b = Block(0,"HQ27716",[])
chain1 = BLKchain()
chain1.add_genblock()
#chain1.add_block(chain1.lasthash, "HQ265512", [])
chain1.unconfirmed_trans=["eqweqw"]
chain1.mine("H29918")
chain1.show()
