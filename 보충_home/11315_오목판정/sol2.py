import sys
sys.stdin = open('input.txt')
# 델타 탐색 없이 가능한가? 대각 탐색...

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = 0
    cnt = 0

    ans = 'NO'

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            if arr[i][j] == '.':
                cnt = 0
            if cnt >= 5:
                ans = 'YES'

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
            if arr[j][i] == '.':
                cnt = 0
            if cnt >= 5:
                ans = 'YES'



    print(f'#{tc} {ans}')




