import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra(start):
    # 비교 대상이 될 가중치 정보
    dist = [E * 100] * (V+1) # 충분히 큰 값으로 초기화 가중치를
    # 우선순위 큐
    Q = []
    # 출발점 초기화
    heapq.heappush(Q, (0,0)) # 힙 값 삽입시 heap(가중치, 노드번호)
    dist[0] = 0


    # 우리가 맨날 하던 BFS와 다를 게 없다.!!!!!
    
    while Q:
        W, node = heapq.heappop(Q)
        
        # 가중치 정보, 누적정보로
        #  이미 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있는지 확인
        if dist[nodede] < W: continue

        for next in range(len(arr[node])):

            # 갈 수 있는지 판별
            # 내 간선정보의 현재 노드의 다음 인접 노드 번호
            # 출력한 값이 E * 100이 아니면
            if arr[node][next] != E * 100:
                next_node = next
                cost = arr[node][next]

                new_cost = cost + W

                if dist[next_node] <=  new_cost: 
                    continue
                    
                dist[next_node] = new_cost
                heapq.heappush(Q, (new_cost, next_node))

    return dist[V]



        # 인접 노드 모두 조회

            


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[E*100] * (V+1) for _ in range(V+1)]

    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S][E] = W
    print(arr)
    print(dijkstra(0))
