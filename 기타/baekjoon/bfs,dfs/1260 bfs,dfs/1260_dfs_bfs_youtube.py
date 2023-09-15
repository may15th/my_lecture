# import sys
# sys.stdin = open('input.txt')

# T = int(input())
# # print(T)
# for tc in range(1, T+1):

# 아래 덩어리가 dfs 역할
def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1          # 방문 표시

    for n in adj[c]:
        if not v[n]:  # 방문하지 않은 노드인 경우
            dfs(n)

# 아래 덩어리가 bfs역할
def bfs(s):
    q = []              # 필요한 q, v[], 변수 생성
    q.append(s)         # q에 초기데이터(들) 삽입
    ans_bfs.append(s)
    v[s] = 1

    # print(v)

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]: # 방문하지 않은 노드 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


N, M, V = map(int, input().split())
# print(N,M,V)
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)    #양방향

# print('============')
# print(adj)
# print('============')

# [1] 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

# print(adj)

v = [0] * (N+1)
ans_dfs = []
dfs(V)


v = [0] * (N+1)
ans_bfs = []
bfs(V)

# print(ans_dfs)
# print(ans_bfs)

print(*ans_dfs)
print(*ans_bfs)


'''
input
5 5 3
5 4
5 2
1 2
3 4
3 1

output
3 1 2 5 4
3 1 4 2 5

'''