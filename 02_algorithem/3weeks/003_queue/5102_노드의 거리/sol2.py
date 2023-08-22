def bfs(start, cnt):
    q = [(start, cnt)]
    visited[start] = 1
    while q:
        start, cnt = q.pop(0)
        for next in range(V+1):
            if start == G:
                return cnt
            if mat[start][next] == 1 and not visited[next]:
                q.append((next, cnt+1))
                visited[next] + 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    mat = [[0]*(V+1) for _ in range(V+1)]   # 행렬을 node 갯수 +1 만큼 채운다
    visited = [0] * (V+1)
    for _ in range(E):
        n1, n2 = map(int, input().split())
        mat[n1][n2] = 1
        mat[n2][n1] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, 0)}')