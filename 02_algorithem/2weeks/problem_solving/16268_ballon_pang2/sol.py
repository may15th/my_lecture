# import sys
# sys.stdin = open('input.txt')
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split()) for _ in range(N))]
#
# # NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면,
# # 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.
#
# # (3<=N, M<=100)
#
#     for i in range(N):
#         di = [0, 0, 1, 0, -1]
#         dj = [0, 1, 0, -1, 0]
#         sum = 0
#         max_v = 0
#         for j in range(M):
#             for dir in range(5):
#                 ni = i+di[dir]
#                 nj = j+dj[dir]
#                 if ni >= 0 and nj >= 0 and ni <= (N-1) and nj <= (M-1):
#                     print(arr[ni][nj])


    #                 sum += arr[ni][nj]
    #             if max_v < sum:
    #                 max_v = sum
    #
    # print(f'{tc} {max_v}')

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    max_v = 0
    # N, M 행 수, 열 수
    N, M = map(int, input().split())
    # 행렬 값 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 수정된 부분
    for i in range(N):
        #순회 요소 입력 중앙, 우하좌상
        di = [0, 0, 1, 0, -1]
        dj = [0, 1, 0, -1, 0]
        for j in range(M):
            sum = 0                     # sum, max_v 초기화 위치를 어떻게 할 것인가.
            # 좌표값으로 써줄 ni, nj 넣기
            for dir in range(5):
                ni = i+di[dir]
                nj = j+dj[dir]
                # ni, nj
                if 0 <= ni <= (N-1) and 0 <= nj <= (M-1):
                    sum += arr[ni][nj]

            if max_v < sum:
                max_v = sum

    print(f'#{tc} {max_v}')