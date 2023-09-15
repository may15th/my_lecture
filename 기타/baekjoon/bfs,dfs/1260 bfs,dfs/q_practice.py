# 입력할 떄는 list.append(something)이고 list.pop(0) 출력 이렇게 하면 시간복잡도 O(N)이라 비효율적인 코드

# 인접 노드 중 방문하지 않았던 노드를 큐에 넣을 때는 파이썬 데이터 타입 SET이용

# 유향 그래프
graph_list = {1:set([3,4]),
              2:set([3,4,5]),
              3:set([1,5]),
              4:set([1]),
              5:set([2,6]),
              6:set([3,5])
              }
root_node = 1

# bfs

from collections import deque

def BFS_with_adj_list(graph,root):
    visited=[]
    queue=deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph(n)-set(visited)
        return visited

print(BFS_with_adj_list(graph_list, root_node))


#
# def DFS_with_adj_list(graph,root):
#     visited = []
#     stack = [root]
#
#     while stack:
#         n=stack.pop()
#         if n not in visited:
#             visited.append(n)
#