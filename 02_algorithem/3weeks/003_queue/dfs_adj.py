'''
#1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

#2
5 6
1 2 1 3 1 4 2 5 3 5 4 5
'''


def dfs(s, V):
    stack.append(s)
    visited[s] = 1
    while stack:
        t = stack.pop()
        print(t)
        for w in adj_l[t]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)



V, E = map(int, input().split())
arr = list(map(int, input().split()))
#인접 리스트
adj_l = [[] for _ in range(V+1)]
visited = [0] * (V+1)
stack = []
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

dfs(1,5)