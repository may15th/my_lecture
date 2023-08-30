import sys
sys.stdin = open('input.txt')

def dfs(n, sm, cur):
    global ans
    if n == N:
        # 여태까지의 소모량 + 1번으로 복귀비용
        ans = min(ans, sm+arr[cur][1])
        return

    for j in range(2, N+1):
        if visited[j] == 0:
            # 아래 visited[j] = 1,0 대칭인 것 기억
            visited[j] = 1
            dfs(n+1, sm+arr[cur][j], j)
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    # 백트래킹이 뭐야...
    # 중복 방지를 위해 visited 만들어서...
    # 출발지는 무조건 1번, 1로 복귀해야 함.
    # n: 방문한 구역 수
    N = int(input())
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    print(arr)

    # 최대비용이 될 수 있는 값
    ans = 100 * N

    visited = [0] * (N+1)

    dfs(1, 0, 1)
    print(f'#{tc} {ans}')