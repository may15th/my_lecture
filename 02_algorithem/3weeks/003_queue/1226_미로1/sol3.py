import sys
sys.stdin = open('input.txt')


def find_start(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1

    while q:
        i, j = q.pop(0)     # 순서 헷갈릴 수 있는데 앞에서 초기값 넣어주고 지금은 뺴주는 것 아래에서
                            # 다시 넣어줄 것이기 때문에 지금 빼주는 것
        if arr[i][j] == 3:
            return 1

        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        for dir in range(4):
            ni = i +di[dir]
            nj = j +dj[dir]
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != 1 and visited[i][j] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0    # return 0의 위치는 return 1이 없으면 0반환이기 떄문에
                # while문 바깥에 둔다.



for _ in range(1,11):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')