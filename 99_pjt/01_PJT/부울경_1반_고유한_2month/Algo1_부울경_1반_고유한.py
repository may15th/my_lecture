# 테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):
    # 정사각행렬의 행, 열 수 입력
    N = int(input())
    # 행렬 값 입력
    Aij = [list(map(int, input().split())) for _ in range(N)]
    # 우, 하, 좌, 상 탐색을 위한 요소 입력
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 최대, 최소값은 충분히 작은 값, 충분히 큰 값으로 각각 초기화
    max_v = 0
    min_v = 10000

    # 행 열 순회
    for i in range(N):
        for j in range(N):
            # sum_v값 초기화
            sum_v = Aij[i][j]

            # 4방향 순회
            for dir in range(4):
                # 풍선값만큼 4방향 터짐
                for k in range(1, Aij[i][j]+1):
                    ni = i + di[dir] * k
                    nj = j + dj[dir] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_v += Aij[ni][nj]

            # max, min값 구하기
            if sum_v >= max_v:
                max_v = sum_v
            if sum_v <= min_v:
                min_v = sum_v

    ans = max_v - min_v
    print(f'#{tc} {ans}')

