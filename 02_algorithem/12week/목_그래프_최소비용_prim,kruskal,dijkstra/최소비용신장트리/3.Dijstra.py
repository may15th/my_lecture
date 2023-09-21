
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

# 최단거리 문제 유형
# 1. 특정 지점 -> 도착지점까지의 최단 거리: 다익스트라
# 2. 가중치에 음수가 포함되어 있네? : 벨만-포드
# 3. 여러 지점 - 여러 지점까지의 최단 거리 : 플로이드 워샬


# 내가 갈 수 있는 경로 중 누적거리 가장 짧은 것부터 고르자!
import heapq

# 입력
n, m = map(int, input().split())
# 인접 리스트
graph =[[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t,w])  # 양방향 아님. 단방향이라 이렇게 코딩

print(graph)

# 1. 누적거리를 계속 저장
INF = int(1e9) # 최대값으로 1억 - 대충 엄청 큰 수
distance = [INF] * n

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

        # 돌아돌아 같은 점에 왔는데 더 짧은 경우 있을 수 있으므로
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
         # 다익스트라 확인사항 - 2. 그래프에는 무엇을 저장해 놨고
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost

            # dist는 now까지 온 누적거리(weight)
            # cost는 다음 노드로 연결하는 weight

            # 누적거리가 기존보다 크네?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)


 # 다익스트라는 구현할 수 있으려면
 # 1.pq를 왜쓰는지 무엇을 저장해놨는지
 # 2. 그래프에는 무엇을 저장해 놨고
 # 3. pq에는 무엇을 저장해놨는지
 # 4. 내가 가지치기처럼 보지 말아야 할 건 무엇인지 잘 생각해야 함.