import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # n 손님수, m m초동안 k k개 붕어빵 만듬
    N, M, K = map(int, input().split())
    # 손님 n명이 각각 도착하는 시간
    arr = list(map(int, input().split()))
    # 도착하는 순서대로 정렬
    arr.sort()
    # 손님이 붕어빵을 사려면 도착시간 arr[i]까지 누적 손님수 <= arr[i]까지 생산량이
    # 같거나 많아야.

    #결과는 'Possible'일 것 같은데
    result = 'Possible'
    for i in range(N):
        # 이게 어떤 상황인거지?
        if i+1 > arr[i]//M+K:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')
    