import sys
sys.stdin = open('input.txt')
# 테스트 케이스 입력
T = int(input())
# print(T)  # 디버깅용

# 각 테스트 케이스마다 반복문
for t in range(1, T+1):  # 제출할 때 1부터 깔끔하게 나오게
    # 먼저 정류장들을 다 만들어놓고 해당 정류장에 특정 노선이 방문하는지
    # -> bus_stop 정류장
    # 버스정류장은 몇개? 5000.
    # bus_stop = [0] * 5000  # 각각의 인덱스 자리를 정류장으로 보고, 해당 정류장에 방문하면
    bus_stop = [0] * (5000 + 1)  # 인덱스와 우리의 일반적인 숫자 순서는 일치합니까?
    # 하나가 차이나니까 애초에 1칸을 늘려서 -1 빼기 연산을 하지 않는 방향.
    # 0으로 잡혀있는 원소 자리들을 1씩 더해주겠다
    print(f"#{t}", end=" ")
    # 노선의 개수 입력
    N = int(input())  # 버스 노선의 총개수
    # print(N)
    # 노션별 시작지점, 끝지점
    for n in range(N):
        ai, bi = map(int, input().split())
        # print(ai, bi)  # 시작지점, 끝지점
        # 어떠한 노선이 시작지점부터 끝지점까지 방문한다면
        # 해당 범위는 우리가 만든 정류장 리스트에서 슬라이싱을 통해서...
        for i in range(ai, bi+1):  # +1? -> range나 슬라이싱은 끝점을 포함 X
            # +1을 해서 끝점까지 포함시키려고...
            bus_stop[i] += 1  # 1씩 증가시킨다
        # print(bus_stop)
    P = int(input())  # 방문을 확인할 정류장들의 총 개수
    for _ in range(P):  # _ : 반복문에서 임시변수 사용안하겠다
        # range(P) -> P번 찾아주겠다
        p = int(input())  # 각 정류장의 번호
        # 1, 2, 3, 4, 5...로 예시에는 나와 있는데
        # 실제로는 지멋대로 줍니다
        # print("p", p)  # 조회하고자 하는 버스정류장의 번호
        print(bus_stop[p], end=" ")  # 노선이 방문한 횟수
    print()