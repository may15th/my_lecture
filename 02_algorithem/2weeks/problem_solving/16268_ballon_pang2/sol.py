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

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 수정된 부분

    for i in range(N):
        di = [0, 0, 1, 0, -1]
        dj = [0, 1, 0, -1, 0]
        for j in range(M):
            sum = 0
            max_v = 0
            for dir in range(5):
                ni = i+di[dir]
                nj = j+dj[dir]
                if 0 <= ni < N and 0 <= nj < M:
                    sum += arr[ni][nj]
                if max_v < sum:
                    max_v = sum

    print(f'#{tc} {max_v}')