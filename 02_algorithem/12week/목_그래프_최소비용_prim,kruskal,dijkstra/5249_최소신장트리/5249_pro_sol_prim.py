import sys
sys.stdin = open('input.txt')
import heapq

def prim():
    # Q 생성
    Q = [(W, next) for next, W in G[0]]
    # 방문 표시 
    visited = [0] * (V+1)
    visited[0] = 1

    heapq.heapify(Q)
    #시작 가중치 = 0으로 초기화 해놓고
    acc = 0

    while Q:
        # 가장 작은 가중치를 가진 노드 먼저 순회
        W, now = heapq.heappop(Q)
        # 아직 방문한 적 없으면
        if not visited[now]:
        # 가중치를 기록 할 수 있어야 할듯?
            acc += W
            visited[now] = 1
            # 다음 조사 대상 노드 Q에 추가
            # *************prim 방식
            # ************ prim방식 어렵게 생각 x 우선순위 q랑 자료구조만 잘 이해하면 너비우선 탐색 활용하면 쉽게 풀린다.
            for next, W in G[now]:
                if not visited[next]:
                    heapq.heappush(Q, (W,next))

    return acc




T = int(input())




for tc in range(1, T+1):
    V,E = map(int, input().split())
    arr = [list(map(int, input().split()) for _ in range(E))]
    G = [[] for _ in range(V+1)]
    for i in range(E):
        G[arr[i][0]].append[[arr[i][1], arr[i][2]]]
        G[arr[i][1]].append[[arr[i]]]