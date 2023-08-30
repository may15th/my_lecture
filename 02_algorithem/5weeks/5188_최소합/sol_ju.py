import sys
sys.stdin = open('input.txt')

T = int(input())
di = [0, 1]
dj = [1, 0]

def dfs(i, j):
    global res, tmp
    if res < tmp:   # 현재 결과값 보다 크면 함수 끝나도록 -> 제한 시간 때문에 가지치기 해야함.
        return
    if i == N-1 and j == N-1:
        res = tmp
        return
    for d in range(2):
        ni = i +di[d]
        nj = j +dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj>=N:
            continue

        if (ni,nj) not in visited:
            visited.append((ni,nj))     #좌표 업로드
            tmp += arr[ni][nj]
            dfs(ni,nj)
            tmp -= arr[ni][nj]    #원상복구
            visited.remove((ni,nj))



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    res = 3000
    tmp = arr[0][0]
    dfs(0, 0)    #현재좌표
    print(f'#{tc} {res}')