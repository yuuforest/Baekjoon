
"""
title  : 15655. N과 M (6) (Silver 3)
time   : 44ms       116ms
memory : 31120KB    108080KB
"""

import sys

def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))

    def make(idx:int, count:int, answer:list):

        if count == M:
            print(" ".join(answer))
            return
        
        for jdx in range(idx+1, N):
            answer.append(str(numbers[jdx]))
            make(jdx, count+1, answer)
            answer.pop()
    
    make(-1, 0, [])

solution()