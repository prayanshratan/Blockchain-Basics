import time
import hashlib

class Block(object):
    
    def __init__(self, index, proof, prev_hash, transactions):
        self.index = index 
        self.proof = proof
        self. prev_hash = prev_hash
        self.transactions = transactions
        self.time = time.time() 

    @property
    def get_block_hash(self):
        block_string = '{}{}{}{}{}'.format(self.index, self.proof, self.prev_hash, self.transactions, self.time)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_node_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.create_new_block(proof=0, prev_hash=0)

    def create_new_block(self, proof, prev_hash):
        block = Block(
            index = len(self.chain),
            proof = proof,
            prev_hash = prev_hash,
            transactions = self.current_node_transactions
        )
        self.currrent_node_transactions = []

        self.chain.append(block)
        
    
    def create_new_transactions(self, sender, reciever, amount):
        self.current_node_transactions.append({
            'sender' : sender,
            'reciever' : reciever,
            'amount' : amount
        })
        return self.get_last_block.index+1


    @staticmethod
    def create_proof_of_work(prev_proof):
        proof = prev_proof + 1
        while(proof + prev_proof) %7 != 0:
            proof += 1
        return proof

    @property
    def get_last_block(self):
        return self.chain[-1]

blockchain = Blockchain()
print ('Before Mining >>>>')

last_block = blockchain.get_last_block
last_proof = last_block.proof
proof = blockchain.create_proof_of_work(last_proof)

blockchain.create_new_transactions(
    sender = '0',
    reciever ='address_x', 
    amount = 1
)

last_hash = last_block.get_block_hash
block = blockchain.create_new_block(proof, last_hash)

print('After Mining >>>>')
print(blockchain.chain)

from uuid import uuid4
from flask import Flask, jsonify

app = Flask(__name__)

blockchain = Blockchain()
node_address = uuid4().hex

@app.route('/create-transaction', methods = ['POST'])
def create_transaction():
    transaction_data = request.get_json()

    index = blockchain.create_new_transactions(**transaction_data)

    response = {
        'message' : 'Transaction has been submitted successfully',
        'block_index' : index
    }
    return jsonify(response), 201


@app.route('/mine', methods = ['GET'])
def mine():
    block = blockchain.mine_block(node_address)

    response = {
        'message' : 'Successfully mined the new block',
        'block_data' : block 
    }
    return jsonify(response)
    

@app.route('/chain', methods = ['GET'])
def get_full_chain():
    response = {
        'chain' : blockchain.get_serialized_chain
    }
    return jsonify(response)

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-H', '--host', default='127.0.0.1')
parser.add_argument('-p', '--port', default=5000, type=int)
args = parser.parse_args()

app.run(host = args.host, port = args.port, debug = True)  