T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    sum = 0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for i in range(n):
        for j in range(m):
            sum = arr[i][j]
            for dir in range(4):
                for k in range(1, arr[i][j]+1):
                    ni = i + di[dir]*k
                    nj = j + dj[dir]*k
                    if 0<=ni<n and 0<=nj<m:
                        sum += arr[ni][nj]
        if sum >= max:
            max = sum

    print(f'#{tc} {max}')