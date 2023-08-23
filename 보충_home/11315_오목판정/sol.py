import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'

    # 이게 더 깔끔한 팡션이네
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
            else:
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
            else:
                cnt = 0

    print(f'#{tc} {ans}')
