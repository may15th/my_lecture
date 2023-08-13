T = 1
for tc in range(1, T+1):
    # N, M 행 수, 열 수
    # N, M = map(int, input().split())
    N, M = 3, 5
    # 행렬 값 입력
    #arr = [list(map(int, input().split())) for _ in range(N)]  # 수정된 부분
    arr = [[2, 1, 1, 2, 2],
           [2, 2, 1, 2, 2],
           [2, 2, 1, 1, 2],
           ]

    max_v = 0
    for i in range(N):
        #순회 요소 입력 중앙, 우하좌상
        di = [0, 0, 1, 0, -1]
        dj = [0, 1, 0, -1, 0]
        for j in range(M):
            sum = 0
                   # sum, max_v 초기화 위치를 어떻게 할 것인가.
                            # i, j가 매 요소 값 생성할 떄마다 초기화 시켜줘야함.
            # 좌표값으로 써줄 ni, nj 넣기
            for dir in range(5):
                ni = i+di[dir]
                nj = j+dj[dir]
                # ni, nj
                if 0 <= ni <= (N-1) and 0 <= nj <= (M-1):
                    sum += arr[ni][nj]
            #print(sum)            # print위치 직관적으로 쓸 수 있도록 암기,
        if max_v < sum:
            max_v = sum         # 반복문 끝나는 곳에 print 놓는다.

            print(max_v)        # 진짜 위치 잡기 개어렵네 ㅋㅋㅋㅋㅋㅋ
                                # 이렇게 할 경우 i 순회하면서 최댓값추출??
                                # print