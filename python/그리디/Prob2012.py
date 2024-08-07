
""" 실버 3. 등수 매기기 """

import sys

def solution():
    input = sys.stdin.readline

    N = int(input())
    grade = sorted([0] + [int(input()) for _ in range(N)])

    # answer = 0
    # for idx in range(N):
    #     answer += abs(idx + 1 - grade[idx])

    # return answer

    return sum(abs(idx - g) for (idx, g) in enumerate(grade))

print(solution())