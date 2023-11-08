'''
3
3
10 70 30
40 50 20
60 90 100
3
10 20 0
0 40 60
70 80 0
2
30 29
32 30


'''
# 테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):

    # 백트래킹 함수 dfs
    def dfs(n, sum):
        global max_v

        # n == N 탐색 마칠 경우, 이전 max_v값과 비교해서 더 큰 값 추출.
        if n == N:
            max_v = max(max_v, sum)
            return

        # dfs(n+1, sum +S[n][j]) 재귀 함수 호출하면서 행이동, for문으로 열 이동 하면서 sum값을 더해줌.
        # 이때 이전 행에서 이미 방문했던 열은 visited[j] = 1로 표시되어 다시 방문하지 않음.
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(n+1, sum + S[n][j])
                visited[j] = 0


    # 과녁 행,렬 값 N, 과녁점수 S를 2중 list로 받아줌
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    # 방문한 지점 표시해주는 visited, 최대값 구해주는 max_v 0으로 초기화
    visited = [0] * N
    max_v = 0
    # 백트래킹 함수 dfs 호출
    dfs(0, 0)

    print(f'#{tc} {max_v}')
