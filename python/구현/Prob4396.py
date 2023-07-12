
""" 실버 4. 지뢰 찾기 """


N = 0           # 지뢰판의 크기
Board = []      # 지뢰판

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# --------------------------------------------------------------------------------

def doCountStart(r, c):

    count = 0
    
    for num in range(8):
        
        nr = r + dr[num]
        nc = c + dc[num]

        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        
        if Board[nr][nc] == '*':
            count += 1

    return count

# --------------------------------------------------------------------------------

N = int(input())

# Board = []
Board_clicked = []      # 클릭한 지뢰판

for num in range(N):                                # 지뢰판
    Board.append(list(input()))
for num in range(N):                                # 클릭한 지뢰판
    Board_clicked.append(list(input()))

# --------------------------------------------------------------------------------

flag = False    # 지뢰 클릭 여부

for r in range(N):
    for c in range(N):

        # 클릭 안한 칸
        if Board_clicked[r][c] == '.':
            continue

        # 클릭한 칸

        if Board[r][c] == '.':                          # 지뢰가 없는 칸
            Board_clicked[r][c] = doCountStart(r,c)

        elif Board[r][c] == '*' and not flag:            # 지뢰가 있는 칸
            flag = True
            for n1 in range(N):
                for n2 in range(N):
                    if Board[n1][n2] == '*': 
                        Board_clicked[n1][n2] = '*'

for row in Board_clicked:
    for col in row:
        print(col, end="")
    print()