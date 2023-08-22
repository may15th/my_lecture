import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    q = [(i, j)]
    while q:
        i, j = q.pop(0)
        for dir in range(4):
            ni = i +di[dir]
            nj = j +dj[dir]
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] !=1:
                if arr[ni][nj] == 3:
                    return 1
                arr[ni][nj] = 1
                q.append((ni, nj))
    return 0

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                print(f'#{tc} {bfs(i, j)}')