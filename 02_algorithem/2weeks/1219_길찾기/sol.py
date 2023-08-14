#인접 행렬 사용
import sys
sys.stdin = open('input.txt')


for tc in range(10):
    t, E = map(int, input().split())
    edge_input = list(map(int, input().split()))
    edge_matrix = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(E):
        start_node = edge_input[i*2]
        end_node = edge_input[i*2+1]
        edge_matrix[start_node][end_node] = 1

    stack = [0]
    visited = [False] * 100

    # stack에 있는 것들 하나씩 pop하면서 완전 탐색
    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

            #now에 연결된 v들 stack에 push하는 과정 다push함
            for v in range(100):
                if not visited[v] and edge_matrix[now][v] == 1:
                    stack.append(v)

    if visited[99]:
        result = 1
    else:
        result = 0
    print(f'#{t} {result}')
