#!/usr/bin/env python3

def print_fibonacci(length):
    seq = [0, 1]
    
    while len(seq) < length:
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    
    print(seq[:length])