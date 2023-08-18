# 앞 뒤로 추가와 삭제가 가능한 양방향 큐(deque)
from collections import deque

# def bfs(start, end):
#     # 시작점 설정 및 방무너리




for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 그래프 표시할 2차원 행렬
    arr = [[] for _ in range(V+1)]  #이건 어떻게 표시되는 거지?

    # 방향이 없는 그래프이므로 양방향 설정
    for i in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    start, end = map(int, input().split())