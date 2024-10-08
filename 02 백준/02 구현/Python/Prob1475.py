
"""
title  : 1475. 방 번호 (Silver 5)
time   : 44ms      120ms
memory : 33240KB   108080KB
"""

import sys
import math

def solution():
    input = sys.stdin.readline

    N = input().rstrip()    # 방 번호
    numbers = [0] * 9       # 0 1 2 3 4 5 6 7 8

    for n in N:
        num = int(n)
        numbers[6 if num == 9 else num] += 1

    numbers[6] = math.ceil(numbers[6] / 2)

    return max(numbers)

print(solution())