import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'
    cnt = 0

    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]

    # 행우선 탐색
    for i in range(N):
        for j in range(N):
            # 'o'인 값을 만나면 우,우대각,하,좌대각 조사
            cnt = 0
            if arr[i][j] == 'o':
                # cnt += 1            # 이 부분 때문에... 이부분을 없애고
                for dir in range(4):
                    cnt = 0     # 방향 바꿀때마다 cnt = 0으로 변해야 함을 꼭 기억!!!!!!!
                    for k in range(1, 5):
                        ni = i+di[dir]*k
                        nj = j+dj[dir]*k
                        if 0<=ni<N and 0<=nj<N:
                            if arr[ni][nj] == 'o':
                                cnt +=1
                                if cnt >= 4:        #cnt가 4이상인 경우로 바꿈
                                    ans = 'YES'

    print(f'#{tc} {ans}')