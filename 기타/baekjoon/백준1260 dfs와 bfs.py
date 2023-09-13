N,M,V = map(int, input())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e =map(int, input())
    adj[s].append(e)
    adj[e].append(s)    #양방향

# [1] 오름차순 정렬
for i in range(1,N+1):
    adj[i].sort()

v = [0] *(N+1)



