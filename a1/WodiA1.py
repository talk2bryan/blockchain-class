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
Mined block hash:  00c0567d28b2593c71b7da4a9ba44c4d171a4d32e7176c2d5af921b7b137ab0f
Mining this block took 0.0008437633514404297 seconds
Started mining block with data: BryanWodi, difficulty: 000
Mined block hash:  000791019bf32227bfbbb99284f4d61c00102b515787ab69653ec8ce84d42784
Mining this block took 0.011893749237060547 seconds
Started mining block with data: BryanWodi, difficulty: 0000
Mined block hash:  0000daa03fabc1e2376694fe876f17d17c6fbbb3cf0e744be78f6c100777f9cd
Mining this block took 0.25539684295654297 seconds
Started mining block with data: BryanWodi, difficulty: 00000
Mined block hash:  00000d193e053665029d5ff7c06553e32487a9537ddfa1a629ff258001578138
Mining this block took 10.553561687469482 seconds
Started mining block with data: BryanWodi, difficulty: 000000
Mined block hash:  000000dda38f9c4b45f67d086e98b96513e391348da1edc9734c1441bf120350
Mining this block took 60.513511657714844 seconds
Mining has taken longer than 30 seconds, stopping...


Printing Blockchain
----------------------------------------------------------------------------
Block Hash: 50263ffd9137935e511273a4c9a1e269f8f3f748515b825c5eaa43f20a3ae8b8
Block Number: 0
Block Data: Genesis Block
Hashes: 0
----------------------------------------------------------------------------
Block Hash: 00c0567d28b2593c71b7da4a9ba44c4d171a4d32e7176c2d5af921b7b137ab0f
Block Number: 1
Block Data: BryanWodi
Hashes: 115
----------------------------------------------------------------------------
Block Hash: 000791019bf32227bfbbb99284f4d61c00102b515787ab69653ec8ce84d42784
Block Number: 2
Block Data: BryanWodi
Hashes: 971
----------------------------------------------------------------------------
Block Hash: 0000daa03fabc1e2376694fe876f17d17c6fbbb3cf0e744be78f6c100777f9cd
Block Number: 3
Block Data: BryanWodi
Hashes: 32415
----------------------------------------------------------------------------
Block Hash: 00000d193e053665029d5ff7c06553e32487a9537ddfa1a629ff258001578138
Block Number: 4
Block Data: BryanWodi
Hashes: 1634268
----------------------------------------------------------------------------
Block Hash: 000000dda38f9c4b45f67d086e98b96513e391348da1edc9734c1441bf120350
Block Number: 5
Block Data: BryanWodi
Hashes: 7370657
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

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.block_num = self.block.block_num + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block, difficulty):
        print("Started mining block with data: {}, difficulty: {}".format(block.data, difficulty))
        for n in range(self.max_nonce):
            if (block.hash()).startswith(difficulty):
                block.block_hash = block.hash()
                self.add(block)

                print("Mined block hash: ", block.block_hash)
                
                break
            else:
                block.nonce += 1


# Main:
if __name__ == "__main__":
    blockchain = Blockchain()
    num_zeroes = 2
    max_mining_time_seconds = 30
    
    start_time = time.time()
    while True:
        blockchain.mine(Block("BryanWodi"), "0"* num_zeroes)
        run_time = time.time() - start_time
        print("Mining this block took {} seconds".format(run_time))
        if (run_time > max_mining_time_seconds):
            print("Mining has taken longer than {} seconds, stopping...".format(max_mining_time_seconds))
            break
        
        num_zeroes += 1

    print("\n\nPrinting Blockchain")
    print("----------------------------------------------------------------------------")
    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next

    print("\nEnd of processing.\nAuthor: Bryan Wodi")