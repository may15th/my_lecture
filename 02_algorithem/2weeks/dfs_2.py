'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

output
1 2 4 6 5 7 3
'''


def DFS(node):
    stack = [node]
    visited = [False] *(V+1)
    result_list = []
#stack에서 pop해준다
    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True
            result_list.append(now)
        for v in range(V+1):
            if not visited[v] and edge_matrix[now][v] == 1:
                stack.append(v)

    result = list(map(str, result_list))
    return result

V, E = map(int, input().split())
edge_input = list(map(int, input().split()))
edge_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    start_node = edge_input[i*2]
    end_node =  edge_input[i*2+1]
    edge_matrix[start_node][end_node] = 1
    edge_matrix[end_node][start_node] = 1

result = ' '.join(DFS(1))
print(result)
