
"""
title  : 11501. 주식 (Silver 2)
time   : 3608ms        1444ms
memory : 167252KB      328792KB
"""

import sys

def solution():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):

        N = int(input())                            # 날의 수
        board = list(map(int, input().split()))     # 날 별 주가

        max_value = board[-1]
        idx = len(board) - 1

        answer = 0
        while idx >= 0:

            answer += (max_value - board[idx] if max_value > board[idx] else 0)

            max_value = max(max_value, board[idx])
            idx -= 1

        print(answer)

solution()