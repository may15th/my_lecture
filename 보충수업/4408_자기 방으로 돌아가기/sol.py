import sys
sys.stdin = open('input.txt')

# 복도를 기준으로 번호를 정해보자

T = int(input())
for tc in range(1, T+1):
    N = int(input())      #학생 수
    arr = [list(map(int, input().split()))]

    #복도를 나타내는 카운트 배열 필요
    cnt = [0] * 201 # 방 사이 공간을 지나는 사람 수
    for a, b in arr:    # arr에서 a,b 구할 거니까  a<=b 라는 보장이 없음.
        for i in range(min(a,b), max(a,b)+1)

