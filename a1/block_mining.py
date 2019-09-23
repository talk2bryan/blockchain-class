#!/usr/bin/env python3

# Adapted from GitHub Tutorial: Simple-Python-Blockchain/blockchain.py
'''
Programming Assignment 1
Author: Bryan Wodi
Instructor: Cuyent A.
Course: COMP 7570 - Blockchain Analysis
Date: September 22, 2019
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
            print("Started mining block, difficulty: " + difficulty)
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
    num_zeroes = 6
    # max_mining_time_seconds = 2

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for n in range(2, num_zeroes+1):
            executor.submit(blockchain.mine, Block("BryanWodi"), "0"* (n))


    # while True:
    #     thread_process = multiprocessing.Process(difficulty=timed_mining, name="MineBlock", args=(Block("BryanWodi"), "0"* num_zeroes))
    #     thread_process.start()

    #     time.sleep(max_mining_time_seconds)

    #     if thread_process.is_alive():
    #         print("Mining this block took longer than {} seconds, stopping...".format(max_mining_time_seconds))
    #         thread_process.terminate()
    #         thread_process.join()
    #         break
    #     # thread_process.join()
    #     num_zeroes += 1

    print("\n\nPrinting Blockchain")
    print("----------------------------------------------------------------------------")
    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next


    

