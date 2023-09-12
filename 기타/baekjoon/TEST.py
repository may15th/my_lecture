M = 3
adj = [[] for _ in range(4)]

for _ in range(M):
    s, e =map(int, input())
    adj[s].append(e)
    adj[e].append(s)