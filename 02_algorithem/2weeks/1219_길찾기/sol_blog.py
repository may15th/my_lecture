import sys
sys.stdin = open('input.txt')


for tc in range(10):
    t, E = map(int, input().split())
    edge_list = list(map(int, input().split()))
    edge_matrix = [[0]*100 for _ in range(100)]

    for i in range(E):
        start_node = edge_list[i * 2]
        end_node = edge_list[i * 2 + 1]
        edge_matrix[start_node][end_node] = 1

    visited = [False]*100
    stack = [0]     #0에서 시작하기 때문에 0으로 넣어준 것.

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

            for v in range(100):
                if not visited[v] and edge_matrix[now][v] == 1:
                    # 방문 안했고 edge_matrix가 1(연결돼있다면)
                    stack.append(v)

    if visited[99]:
        result = 1
    else:
        result = 0
    print(f'#{t} {result}')