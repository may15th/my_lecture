import sys
sys.stdin = open('input.txt')

B = 1   # 흑돌 1
W = 2   # 백돌 2

T = int(input())
for tc in range(1, T +1):
    N, M = map(int, input().split())    #N 보드크기, M 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]
    # 어떻게 해야 할지 모르겠으면 일단 0으로 채워
    board = [[0] * N for _ in range(N)] # 0-> N-1까지 인덱스 사용
    # 중심부 4개의 돌 배치,
    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2-1] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W

    for col, row, bw in play: # 입력이 col, row, color 순임을 기억 col, row는 인덱스 1 기준
        f(row-1, col-1, bw, N)

