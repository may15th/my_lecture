# 델타 탐색, BFS탐색
# bfs,dfs 둘다 상관 없지만, 모든 상황에 대해서 이동을 하므로, bfs
# 단순 bfs문제라고 함.
# 완전 검색 문제이고, 완전 검색말고는 방법이 없다고 함.


import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def BFS():
    Q = deque
    # x,y 삽입 : 시작 좌표는 항상 0,0
    Q.append((0,0))
    visited[0][0] = 0

    while Q:
        x,y = Q.popleft()
        # 4방향 조사
        for k in range(4):
            # 다음 좌표\
            nx = x +dx[k]
            by = y +dy[k]
            # 다음 좌표가 범위 내에 있고, 목적지 좌표의 방문 표시값보다 작거나 같은 경우
            # 분기 : 현재 위치가 다음 위치보다 낮거나 높은 것
            
            if 0<= nx < N and 0<=ny < N and visited[nx][ny] <=visited[N-1][N-1]:
                # 분기 : 현재 위치가 다음 위치보다 낮거나 높은 것.            
                if data[x][y] >= arr[nx][ny]:
                    # 기본 비용만 소모
                    # 다음 칸의 방문 표시값을 현재 표시값이랑 비교

            else:
                if visited[nx][ny] > visited[x][y] +1 +(arr[nx][ny]-arr[x][y]):
                    visited[nx][ny] = visited[x][y] +1
                    Q.append((nx,ny))
                # 높이 차에 대한 비용도 함께 소모
                




T = int(input())
for tc in range(1, T + 1):
    N =int(input())
    arr = [list(map(int, input().split()))]
    print(arr)

    # 비교대상, 모든 데이터를 다 더한 것.
    max_val = sum(sum(arr, []))+ N**2
    # 이전에 방묺나 적이 있다면, 가중치를 visited에 기록
    # 최초 방문시에도, 비교할 수 있는 값이어야 한다. -> 최소 비용을 찾고 있으므로
    visited = [[max_val] * N for _ in range(N)]
    print(visited)