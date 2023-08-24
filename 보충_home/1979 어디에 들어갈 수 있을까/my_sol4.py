import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 행, 열 우선탐색하며 빈 칸 세어주는 변수
    cnt = 0
    # k와 일치하는 빈 칸 덩어리 세어주는 변수
    ans = 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            # (행 시작이 0 or arr[i-1][j]==0) and ( 행 끝이 n or arr[i+K][j] ==0)
            if (0<=i<=N-K) and arr[i-1][j]
                for r in range(i, i+K):
                    if arr[r][j] == 1:
                        cnt += 1
                        if cnt == 3:
                            ans += 1

    for i in range(N):
        for j in range(N):
            cnt = 0
            # (열 시작이 0 or arr[i][j-1]==0) and ( 행 끝이 n or arr[i][j+K] == 0)
            if j == 0 or arr[i][j-1] == 0:
                for c in range(j, j+K):
                    if arr[i][c] == 1:
                        cnt += 1
                        if cnt == 3:
                            ans += 1

    # and (i + K == N or arr[i + K][j] == 0)
    # and (j + K - 1 == N - 1 or arr[i][j + K] == 0)
    print(f'#{tc} {ans}')