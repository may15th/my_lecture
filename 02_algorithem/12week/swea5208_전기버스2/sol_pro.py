import sys
sys.stdin = open('input.txt')

# r: 사용한 원소의 갯수
# acc: 충전 횟수
def search(r, acc, gas):
    global result
    # 종료시점 -> 내 버스가 종점에 도착한 상황
    if r == N-1:
        # 여기까지 오는데 충전 몇 번?
        if acc < result:
            result = acc
    else:
        # 충전 안하고 다음 칸 가기
        search(r+1, acc, gas - 1)
        # 충전 하고 다음 칸 가기
        search(r+1, acc+1, arr[r] - 1)

T = int(input())
for tc in range(1, T+1):
    N, *arr = list(map(int, input().split()))
    # 모든 정류소에서 다 충전한 게 최악의 상황
    result = N
    search[0,0,arr[0]]
    print(result)


    # 백트래킹의 근본은 완전검색 -> 시간초과 -> 유망성조사, 가지치기


