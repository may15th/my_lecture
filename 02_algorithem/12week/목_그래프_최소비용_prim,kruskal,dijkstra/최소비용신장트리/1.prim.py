# 변수, 조건문, 반복문이 알고리즘의 전부
# 여기에 추가된 게 자료구조.
# 현실세계 문제들을 자료구조, 변수, 조건문, 반복문으로 사용하면 됌.

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# heap이란 
# 우선순위 큐를 위하여 만들어진 자료구조. 
# list를 이용하여 heap구현. but, 여기서는 내장함수 heapq 사용한다.abs

# heapq란?
# 그냥 우선순위큐(pq) = heapq 인듯 하다...

import heapq

def prim(start):
    heap = []
    # MST에 포함되었는지 여부
    MST = [0] * V

    #가중치, 정점 정보
    heapq.heappush(heap, (0, start))    # heappush가 어떻게 채워지는거지? 결국 list인데...
    # 누적합 저장
    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 PASS
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight


V, E = map(int, input().split())

# 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w

result = prim(0)
print(f'최소비용 = {result}')

