
"""
title  : 7785. 회사에 있는 사람 (Silver 5)
time   : 168ms     252ms
memory : 42324KB   132596KB
"""

import sys

def solution():

    N = int(sys.stdin.readline())        # 로그에 기록된 출입 기록 수

    answer = {}

    for _ in range(N):
        name, state = sys.stdin.readline().split()
        if state == 'enter':
            answer[name] = 0
        else:
            answer.pop(name)

    for name in sorted(answer.keys(), reverse=True):
        print(name)
        
solution()
