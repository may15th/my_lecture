import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    ans = 0
    N, K = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            # cnt값이 K라면 ans 값을 1씩 더해주는데
            if cnt == K:
                ans += 1
                # 만약 j+1 열에서 값이 1이라면 빈 칸이 K+1칸이 되므로 ans값을 다시 빼준다
                if j <= N-2:
                    if arr[i][j+1] == 1:
                        ans -= 1
            # arr[i][j]가 0이 되는 순간 cnt=0으로 초기화
            if arr[i][j] == 0:
                cnt = 0
        # 다음 행 넘어갈 때 cnt = 0초기화
        cnt = 0

    print(ans)

    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    if j <= N-2:
                        if arr[j+1][i] == 1:
                            ans -= 1
            elif arr[j][i] == 0:
                cnt = 0
            # elif위와 같이 해버리면 cnt!=K일때만 cnt초기화 해버림. if로 바꿔야함.
        cnt = 0

    print(ans)
    print('==========')