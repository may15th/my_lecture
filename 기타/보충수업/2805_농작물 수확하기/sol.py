import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    sum = 0

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    k = n//2
    print(k)
    for i in range(n):
        for j in range(n):
            for l in range(k):
                for dir in range(4):
                    ni = di[dir]*l
                    nj = dj[dir]*l
                    if 0<=ni<n and 0<=nj<0 and visited[ni][nj] == 0:
                        sum += arr[k+ni][k+nj]
                        visited[ni][nj] += 1

    print(visited)
