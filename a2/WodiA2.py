#!/usr/bin/env python3

'''
Programming Assignment 2
Author: Bryan Wodi
Instructor: Cuyent A.
Course: COMP 7570 - Blockchain Analysis
Date: October 18, 2019


To RUN: 
    python3 WodiA2.py


SAMPLE OUTPUT:

Question 1: Every transaction consuming 1 UTXO each:
Starting x at 0% i.e. 0.00, and increasing by 0.001 if UTXOs <= 2500

Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 550, X = 0.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 574, X = 0.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 575, X = 0.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 599, X = 0.40%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 600, X = 0.50%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 624, X = 0.60%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 635, X = 0.70%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 652, X = 0.80%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 665, X = 0.90%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 685, X = 1.00%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 700, X = 1.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 719, X = 1.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 734, X = 1.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 754, X = 1.40%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 770, X = 1.50%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 790, X = 1.60%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 808, X = 1.70%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 828, X = 1.80%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 848, X = 1.90%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 867, X = 2.00%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 889, X = 2.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 913, X = 2.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 932, X = 2.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 957, X = 2.40%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 976, X = 2.50%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1003, X = 2.60%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1027, X = 2.70%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1049, X = 2.80%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1076, X = 2.90%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1106, X = 3.00%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1127, X = 3.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1157, X = 3.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1183, X = 3.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1214, X = 3.40%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1242, X = 3.50%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1272, X = 3.60%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1303, X = 3.70%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1334, X = 3.80%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1366, X = 3.90%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1394, X = 4.00%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1429, X = 4.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1460, X = 4.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1497, X = 4.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1535, X = 4.40%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1569, X = 4.50%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1608, X = 4.60%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1642, X = 4.70%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1686, X = 4.80%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1722, X = 4.90%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1768, X = 5.00%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1805, X = 5.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1848, X = 5.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1892, X = 5.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1938, X = 5.40%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 1983, X = 5.50%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2035, X = 5.60%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2077, X = 5.70%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2128, X = 5.80%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2177, X = 5.90%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2225, X = 6.00%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2283, X = 6.10%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2338, X = 6.20%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2393, X = 6.30%
Did not create at least 2500 UTXOs at the 125th block...UTXOs after block 125 = 2448, X = 6.40%
Found X at block 124... UTXOs = 2504, X = 6.50%

Question 2: Each transaction consumes x UTXO's. Where x is sampled from a normal distribution.
Found X at block 642... UTXOs = 2503.0, X = 0.10%
'''

import math
import numpy as np

BLOCKCHAIN_HEIGHT = 100

BLOCKCHAIN_HEIGHT_MAX_Q1 = 125
BLOCKCHAIN_HEIGHT_MAX_Q2 = 1000

FACTOR = 0.001
NUM_UTXOS = 500
MAX_UTXOS = 2500

NUM_COIN_OUTPUTS = 1
NUM_TRANSXN_OUTPUTS = 2


def block_mining_simulation(initial_utxos, transxn_inputs, max_block_height):
    
    curr_utxos = initial_utxos
    proportion_X = 0.001 # x% of existing UTXO's
    

    while True:
        input_index = 0
        for curr_block in range(BLOCKCHAIN_HEIGHT, max_block_height):
            if (transxn_inputs[input_index] < 0):
                trans_consumed += NUM_COIN_OUTPUTS
            else:
                trans_consumed = math.ceil(proportion_X * curr_utxos) * \
                transxn_inputs[input_index]
            input_index += 1
            trans_created = trans_consumed * NUM_TRANSXN_OUTPUTS + \
                NUM_COIN_OUTPUTS

            curr_utxos = curr_utxos - trans_consumed + trans_created

            if curr_utxos >= MAX_UTXOS:
                break

        if curr_utxos < MAX_UTXOS:
            print(r"Did not create at least {} UTXOs at the {}th block..."
                r"UTXOs after block {} = {}, X = {:.2f}%".format(
                    MAX_UTXOS, max_block_height, max_block_height, curr_utxos,
                    proportion_X*100))
            proportion_X = proportion_X + FACTOR
            curr_utxos = initial_utxos
        else:
            print('Found X at block {}... UTXOs = {}, X = {:.2f}%'.format(curr_block, 
                curr_utxos, proportion_X*100))
            break

# Main:
num_inputs_q1 = 1

inputs_q1 = np.full(
    (BLOCKCHAIN_HEIGHT_MAX_Q1 - BLOCKCHAIN_HEIGHT), num_inputs_q1)
inputs_q2 = np.floor(np.random.normal(2,1,(
    BLOCKCHAIN_HEIGHT_MAX_Q2 - BLOCKCHAIN_HEIGHT)))

''' Question 1'''
print("\nQuestion 1: Every transaction consuming 1 UTXO each:")
print("Starting x at 0% i.e. 0.00, and increasing by {} if UTXOs <= {}\n".format(
    FACTOR, MAX_UTXOS
))
block_mining_simulation(NUM_UTXOS, inputs_q1, BLOCKCHAIN_HEIGHT_MAX_Q1)

''' Question 2'''
print()
print(r"Question 2: Each transaction consumes x UTXO's. Where x is sampled"
    r" from a normal distribution.")

block_mining_simulation(NUM_UTXOS, inputs_q2, BLOCKCHAIN_HEIGHT_MAX_Q2)
