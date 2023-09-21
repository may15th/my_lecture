'''
2 3
0 1 1
0 2 6
1 2 1
'''

'''
output
#1 2
'''
import heapq
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    def dijkstra(start):
        # 2. 우선순위 큐
        pq = []
        # 출발점 초기화
        heapq.heappush(pq, (0, start))
        distance[start] = 0

        while pq:
            # 현재 시점에서
            # 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(pq)

            if distance[now] < dist:
                continue

            # 인접 노드 확인
            for next in graph[now]:
                next_node = next[0]
                cost = next[1]

                #next_node로 가기 위한 누적 거리
                new_cost = dist + cost

                if distance[next_node] <= new_cost:
                    continue
                
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    V, E = map(int, input().split())
    # 인접 리스트
    graph =[[] for _ in range(V)]
    
    for _ in range(E):
        f, t, w  = map(int, input().split())
        graph[f].append([t,w])
    
    print(graph)        
    
    # 누적거리를 계속 저장
    INF = int(1e9)
    distance = [INF] * V


    dijkstra(0)
    print(f'#{tc} distance[1]')