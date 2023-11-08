import sys
sys.stdin = open('input.txt')

# 테스트케이스 입력
T = int(input())
for tc in range(1, T+1):
    # 노선 수 입력
    N = int(input())

    # 버스 정류장 인덱스 5000번까지 생성
    bus_stop = [0] * 5001

    for i in range(N):
        ai, bi = map(int, input().split())
        # print(ai, bi) ## 디버깅용
        for j in range(ai-1, bi):
            bus_stop[j] += 1
            # print(j, bus_stop[j]) ## 디버깅용


    P = int(input())
    print(f'#{tc}', end = ' ')
    for j in range(1, P+1):
        cj = int(input())-1
        print(bus_stop[cj], end=' ')
    # print()
    # print(bus_stop)
    # 테스트 케이스 무조건 2개로 확인해봐야한다.
    # 이번 같은 문제 발생...
