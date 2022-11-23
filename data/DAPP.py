import json
import time
from integrity import integrity_check
import block
import flask
from flask import Flask, jsonify, request
from block import Block
from transaction import *
from chain import *


class DAPP():
    def __init__(self):
        self.contracts = []

    def add_contract(self, c):
        self.contracts.append(c)


DAPP = DAPP()
time1 = time.asctime((2023, 11, 14, 5, 6, 6, 0, 0, 0))
course = contract1('Tom',time1)
DAPP.add_contract(course)
course2 = contract2()
course2.drop('Haowei','ICSI220')
course2.register('Haowei','ICSI220')
course2.showlist()
#h = open('h.txt', 'r').read()
#course.upload_hw('Haowei','ICSI500',h)
#course.chain.show()





