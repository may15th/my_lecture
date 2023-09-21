# 이때까지는 visited로 방문 한 곳만 기록했었는데 D []로 방문 누적거리도 기록, 이를 충분히 큰 값으로 기록했다가 minimum값으로 업데이트 하는 식.
import sys
sys.stdin = open('input.txt')

def dijkstra():
    # 비교 대상이 될 가중치 정보
    dist = [E * 100] * (V+1) # 충분히 큰 값으로 초기화 가중치를
    visited = [0] * (V+1)
    # 시작지점이 항상 0 (해당 문제)
    dist[0] = 0

    # 전수조사하는 코드 만드는 이유는 
    # 병합 소트 병합과정 중에 왼쪽 가장 끝번 오른쪽가장 끝번인 경우만 물색하기 이런 과정이 있었으니까...
    # 모든 상황에 대한 전수조사 할 필요 있어.
    # 템플릿, 레퍼런스 코드로 가져가면돼.

    for _ in range(V):
        next = 0
        min_val = E * 100

        # 최솟값 찾기
        for i in range(V+1):
            if not visited[i] and min_val > dist[i]:
                next = i
                min_val = dist[i]
        visited[next] = 1
        # 모든 노드에 대해서 도착할 수 있는 최소 가중치 갱신
        for j in range(V + 1):
            if not visited[j] and dist[j] > dist[next] + arr[next][j]:
                dist[j] = dist[next] + arr[next][j]

    #가중치 중, 끝번 노드에 저장된 가중치
    return dist[V]

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[E*100] * (V+1) for _ in range(V+1)]

    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S][E] = W
        print(dijkstra())

