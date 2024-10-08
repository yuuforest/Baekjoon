
"""
title  : 2606. 바이러스 (Silver 3)
time   : 72ms       108ms
memory : 34120KB    112004KB
"""

from collections import deque

N = int(input())    # 컴퓨터 수
M = int(input())    # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

computer = [[] for _ in range(N+1)] 

for _ in range(M):
    i, j = map(int, input().split())
    computer[i].append(j)
    computer[j].append(i)

def bfs(start):

    visited = [0] * (N+1)

    queue = deque()

    queue.append(start)
    visited[start] = 1

    while queue:

        now = queue.popleft()

        for i in computer[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

    return visited.count(1) - 1

print(bfs(1))