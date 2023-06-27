
""" 실버 3. 알바생 강호 """

N = int(input())    # 줄 서 있는 사람 수 

tips = [int(input()) for _ in range(N)]     # 주려고 하는 팁

tips.sort(reverse = True)   # 팁이 큰 순서대로 내림차순

answer = 0

for num in range(N):
    tip = tips[num] - num

    if tip > 0:
        answer += tip

print(answer)