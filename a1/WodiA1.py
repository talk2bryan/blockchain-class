#!/usr/bin/env python3

# Adapted from GitHub Tutorial: Simple-Python-Blockchain/blockchain.py
'''
Programming Assignment 1
Author: Bryan Wodi
Instructor: Cuyent A.
Course: COMP 7570 - Blockchain Analysis
Date: September 22, 2019


To RUN: 
    python3 WodiA1.py

SAMPLE OUTPUT:
Started mining block with data: BryanWodi, difficulty: 00
Mined block hash:  00679e53c1246fd7ae58d0ddf55e7a25b17dde8e17048f8b3784f9b577dfa5a4
Started mining block with data: BryanWodi, difficulty: 000
Mined block hash:  0002e0088ccf0ae1f5a4a141ad98d53e71e39f67fe85e5bd9649a2db7e815d60
Started mining block with data: BryanWodi, difficulty: 0000
Mined block hash:  000057657f352462621676f092dc81c7ae7feb9b70c4792ea79e1297b081e9c5
Started mining block with data: BryanWodi, difficulty: 00000
Mined block hash:  00000329522d0175ba8931c94e2f0824929d3d586bc321252b0cedb4dc973d1b
Started mining block with data: BryanWodi, difficulty: 000000
Mined block hash:  000000e5c3cf91fc853607592497b7f72523035d346da549ba1d296fc0976028


Printing Blockchain
----------------------------------------------------------------------------
Block Hash: 0c3cfbe5bcafdcd7ae662a58b1686fee1ff5e88986cfee73e41d7aa7e0b5bd4f
Block Number: 0
Block Data: Genesis Block
Hashes: 0
----------------------------------------------------------------------------
Block Hash: 00679e53c1246fd7ae58d0ddf55e7a25b17dde8e17048f8b3784f9b577dfa5a4
Block Number: 1
Block Data: BryanWodi
Hashes: 58
----------------------------------------------------------------------------
Block Hash: 0002e0088ccf0ae1f5a4a141ad98d53e71e39f67fe85e5bd9649a2db7e815d60
Block Number: 2
Block Data: BryanWodi
Hashes: 2627
----------------------------------------------------------------------------
Block Hash: 000057657f352462621676f092dc81c7ae7feb9b70c4792ea79e1297b081e9c5
Block Number: 3
Block Data: BryanWodi
Hashes: 175921
----------------------------------------------------------------------------
Block Hash: 00000329522d0175ba8931c94e2f0824929d3d586bc321252b0cedb4dc973d1b
Block Number: 4
Block Data: BryanWodi
Hashes: 300712
----------------------------------------------------------------------------
Block Hash: 000000e5c3cf91fc853607592497b7f72523035d346da549ba1d296fc0976028
Block Number: 5
Block Data: BryanWodi
Hashes: 5436232
----------------------------------------------------------------------------

End of processing.
Author: Bryan Wodi


'''

import concurrent.futures
import datetime
import hashlib
import threading
import time

class Block:
    block_num = 0
    data = None
    next = None
    block_hash = None
    constant_hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()


    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode(encoding='utf-8') +
            str(self.data).encode(encoding='utf-8') +
            str(self.previous_hash).encode(encoding='utf-8') +
            str(self.timestamp).encode(encoding='utf-8') +
            str(self.block_num).encode(encoding='utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.block_hash) + \
            "\nBlock Number: " + str(self.block_num) + \
            "\nBlock Data: " + str(self.data) + \
            "\nHashes: " + str(self.nonce) + \
            "\n----------------------------------------------------------------------------"


class Blockchain:    
    max_nonce = 2**32
    block = Block("Genesis Block")
    block.block_hash = block.hash()

    dummy = head = block

    def __init__(self):
        self._lock = threading.Lock()

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.block_num = self.block.block_num + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block, difficulty):
        with self._lock:
            print("Started mining block with data: {}, difficulty: {}".format(block.data, difficulty))
            for n in range(self.max_nonce):
                if (block.hash()).startswith(difficulty):
                    block.block_hash = block.hash()
                    self.add(block)

                    # print("Mined block:", block)
                    print("Mined block hash: ", block.block_hash)
                    
                    break
                else:
                    block.nonce += 1


# Main:
if __name__ == "__main__":
    blockchain = Blockchain()
    num_zeroes = 2
    max_mining_time_seconds = 3
    
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    	while True:
    		executor.submit(blockchain.mine, Block("BryanWodi"), "0"* num_zeroes)
    		
    		run_time = time.time() - start_time
    		print("Mining this block took {} seconds".format(run_time))
    		if (run_time > max_mining_time_seconds):
    			print("Mining this block took longer than {} seconds, stopping...".format(max_mining_time_seconds))
    			break
    		
    		num_zeroes += 1

    print("\n\nPrinting Blockchain")
    print("----------------------------------------------------------------------------")
    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next

    print("\nEnd of processing.\nAuthor: Bryan Wodi")