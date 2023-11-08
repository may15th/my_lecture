# 테스트 갯수 입력
T = int(input())
# 테스트 갯수 만큼 테스트케이스 순회
for tc in range(1, T+1):
    # 리스트 길이 입력
    N = int(input())
    # 리스트 요소 입력
    arr = list(map(int, input().split()))
    # 한 번 튕길때 이동거리 0로 초기화
    bounce_len = 0
    # 튕겨서 얻는 총 값 sum_v = 0으로 초기화
    sum_v = 0
    # N회 반복
    for _ in range(N):
        # 총N번 시행하는데 튕기는 거리는 시행 횟수와 같음 0번쨰면 1칸씩 1번째면 2칸씩 ...n-1번째는 n칸씩 튕김. 총 n회 시행
        bounce_len += 1
        # 튕김 점수 sum_v에 누적합
        # arr 리스트 0번 부터 N-1까지 bounce_len 만큼 이동
        for i in arr[0:N:bounce_len]: # 이게 안되는 이유는 모르겠다... 검색해보니 그냥 range 슬라이싱은 되고 리스트 슬라이싱은 안되는 것 같다.
                                      # 그냥 range슬라이싱 사용해야 된다고 암기!
            sum_v += arr[i]
    print(sum_v)

    # for i in range(N):
    #     for j in arr[0, N, i]:
    #         sum_v += arr[j]
    #
    # if sum_v < 0:
    #     sum_v = 0


    # 이렇게 하면 된다는데...
#수정한 풀이
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     # 점수를 담을 변수 초기화
#     sum_v = 0
#
#     # 한 번 튕길 때마다 해당 위치의 값을 더해줌
#     # for i in range(N):
#     #     for j in range(0, N, i):    #ValueError: range() arg 3 must not be zero 에러 뜸.
#     #                                 # 스텝값 i가 0이 되는 경우 있기 때문.
#     #         sum_v += arr[j]
#
#     for i in range(1, N+1):
#         for j in range(0, N, i):
#             sum_v += arr[j]
#
#     if sum_v < 0:
#         sum_v = 0
#
#     print(f'#{tc} {sum_v}')