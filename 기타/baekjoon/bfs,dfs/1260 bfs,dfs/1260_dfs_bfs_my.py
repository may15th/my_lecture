'''
input
5 5 3
5 4
5 2
1 2
3 4
3 1
'''
'''
ouput
3 1 2 5 4
3 1 4 2 5
'''

# 아래 인접 리스트 이용한 dfs는 그냥 외워야 함.
def dfs(c):
    v[c] = 1
    ans_dfs.append(c)
    for i in adj[c]:
        if v[i] ==0:
            dfs(i)


def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

print(adj)

for i in range(N+1):
    adj[i].sort()

print(adj)

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0] *(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)











