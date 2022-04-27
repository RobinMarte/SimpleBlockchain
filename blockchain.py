import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block


    def hash_block(self):
        """ Creates hash"""
        sha = hasher.sha256()
        to_hash = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        sha.update(to_hash.encode())

        return sha.hexdigest()


def genesis_block():
    """ Creates a Genesis Block """
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    """ Generates succeeding blocks"""
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "(This is block #" + str(this_index) + ")"
    this_hash = last_block.hash()

    return Block(this_index, this_timestamp, this_data, this_hash)


blockchain = [genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 10


for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Timestamp: {}".format(block_to_add.timestamp))
    print("Data: {}".format(block_to_add.data))
    print("Previous block's hash: {}".format(block_to_add.previous_hash))
    print("Hash: {}\n".format(block_to_add.hash()))