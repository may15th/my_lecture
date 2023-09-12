import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    l = M//2
    arr = [list(input()) for _ in range(N)]

    print(arr)

    # 리스트 슬라이싱 이동하는 방법
    for i in range(N):
        for j in range(N-(M-1)):
            # print(arr[i][j:j+M])  # 리스트 슬라이싱 차례로 이동시키는 방법








