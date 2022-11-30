from flask import Flask, request
from chain import BLKchain
from flask_cors import CORS


import json
from chain import *
from transaction import transaction

app = Flask(__name__)
CORS(app)

time1 = time.time()

contract_1 = contract1('newcontract', time1 )

contract_2 = contract2()
blockchain = BLKchain()
blockchain.add_genblock()

# address
peers = set()

@app.route('/')
def index():
    return "hello world"



@app.route('/course', methods=['POST'])
def getCourse():
    studentID = request.json
    courseInfo = contract_2.showlist()

    # print(courseInfo)
    result = [info for info in courseInfo if info[0] == studentID['studentId']]
    # result = [["studentID","course1"],["studentID","course12"]]
    if result == []:
        return "Cant find course info", 404
    else:
        return result

@app.route('/regist', methods =['POST'])
def get_regist():
    registInfo = request.json
    contract_2.register(registInfo['id'], registInfo['courseName'])
    courseInfo = contract_2.showlist()
    # courseInfo = contract_2.search(registInfo['id'])
    # print(courseInfo)
    # contract_2.chain.show()
    # contract_2.chain.show()
    return courseInfo

@app.route('/drop', methods =['POST'])
def get_drop():
    registInfo = request.json
    contract_2.drop(registInfo['id'], registInfo['courseName'])
    courseInfo = contract_2.showlist()
    # courseInfo = contract_2.search(registInfo['id'])

    # print(courseInfo)

    return courseInfo

@app.route('/settime', methods=['POST'])
def get_time():
    # add_genblock()
    setTime = request.json
    time1 = setTime['Date'] +" "+ setTime['Time'] + ":00"
    print(time1)
    contract_1.deadline = time1
    # contract_1 = contract1.deadline('newcontract', time1 )
    return "ok"

# get the chain information and display chain
@app.route('/chain', methods=['GET'])
def get_chain():
    # add_genblock()
    data = contract_1.check_all_hw()
    return data

@app.route('/uploadhomework', methods = ['POST'])
def homework():
    test1 = request.form
    reqFil =request.files['file'].read()
    Input = reqFil.decode()

    InfoID = test1['studentId']
    Course = test1['course']
    output = contract_1.upload_hw(InfoID,Course,Input)
    if(output == "Homeworklate"):
        return "You can not submit late work", 400
    if(output == "HomeworkCheat"):
        return "Your homewrok cheats", 400
    else:
        return "ok"

# request for a mine service, need to add transaction(unconfirmed)
@app.route('/mine', methods=['GET'])
def mine_unconfirmtrans():
    result = blockchain.mine()
    return json.dumps(result)

# @app.route('/test', methods=['GET'])
# def mine_unconfirmtrans():
#     result = blockchain.show()
#     return json.dumps(result)
