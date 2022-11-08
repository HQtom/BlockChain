from flask import Flask
from chain import BLKchain
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

blockchain = BLKchain()
blockchain.add_genblock()

# address
peers = set()

@app.route('/')
def index():
    return "hello world"

# add new transaction (posts) to the blockchain
@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    data = request.get_json()
    fields = ["ID", "msg"]

    for field in fields:
        if not data.get(field):
            return "Invalid transaction", 404
    data["time"] = time.time()
    trans = transaction(data[0],data[1],data[2])
    blockchain.addtransaction(trans)

    return "request success", 201

# get the chain information and display chain
@app.route('/chain', methods=['GET'])
def get_chain():
    data = blockchain.show()
    test = json.dumps([{"t_stamp": "Mon Nov 7 18:11:43 2022", "p_hash": 1, "ID": 0, "trans": {"sender": "0", "recipient": "", "value": 0, "time": "Mon Nov 7 18:11:43 2022"}, "hash": "9b7c03bb07f51eb1bff20e42d176ba79d7934a25207615f21d03f29174333cf7", "nonce": 0},
    {"t_stamp": "Mon Nov 7 18:11:44 2022", "p_hash": 2, "ID": 1, "trans": {"sender": "1", "recipient": "", "value": 0, "time": "Mon Nov 7 18:11:44 2022"}, "hash": "9b7c03bb07f51eb1bff20e42d176ba79d7934a25207615f21d03f29174333cf8", "nonce": 0},
    {"t_stamp": "Mon Nov 7 18:11:45 2022", "p_hash": 3, "ID": 2, "trans": {"sender": "2", "recipient": "", "value": 0, "time": "Mon Nov 7 18:11:45 2022"}, "hash": "9b7c03bb07f51eb1bff20e42d176ba79d7934a25207615f21d03f29174333cf9", "nonce": 0}])

    return test
    # return json.dumps({"num of blocks": len(data), "chain": data, "peers": list(peers)})


# request for a mine service, need to add transaction(unconfirmed)
@app.route('/mine', methods=['GET'])
def mine_unconfirmtrans():
    result = blockchain.mine()
    return result