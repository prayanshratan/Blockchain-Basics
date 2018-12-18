import hashlib, json

#initial Block (i.e. genesis block)
block_genesis = {
    'prev_hash' : None,
    'transactions' : [1, 3, 4, 2]
}

block_genesis_serialized = json.dumps(block_genesis, sort_keys = True).encode('utf-8')
block_genesis_hash = hashlib.sha256(block_genesis_serialized).hexdigest()

#Block 2
block_2 = {
    'prev_hash' : block_genesis_hash,
    'transactions' : [3, 3, 3, 8, 7, 12]
}

block_2_serialized = json.dumps(block_2, sort_keys = True).encode('utf-8')
block_2_hash = hashlib.sha256(block_2_serialized).hexdigest()

#Block 3
block_3 = {
    'prev_hash' : block_2_hash,
    'transactions' : [3, 4, 4, 8, 34]
}

block_3_serialized = json.dumps(block_3, sort_keys = True).encode('utf-8')
block_3_hash = hashlib.sha256(block_3_serialized).hexdigest()

#Checking previous hashes
def hash_blocks(blocks):
    prev_hash = None
    for block in blocks:
        block['prev_hash'] = prev_hash
        block_serialized = json.dumps(block, sort_keys = True).encode('utf-8')
        block_hash = hashlib.sha256(block_serialized).hexdigest()
        prev_hash = block_hash
    return prev_hash

print('Original Hash')
print(hash_blocks([block_genesis, block_2, block_3]))

print('Tampering the data')
block_genesis['transactions'][0] = 3

print('After being tampered')
print(hash_blocks([block_genesis, block_2, block_3]))








