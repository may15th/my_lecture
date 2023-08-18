def bfs()
    visited = [[0]* N for _ in range(N)]
    visited



def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                i,j = sti,stj


T= int(input())
for tc in range(1, T+1):
    N = 16
    arr = [list(map(int,input())) for _ in range(N)]


    result = bfs()


    print(f'#{tc} {result}')