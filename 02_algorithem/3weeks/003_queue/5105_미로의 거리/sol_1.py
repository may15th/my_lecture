'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
'''
#1 5
#2 5
#3 0
'''
import sys
sys.stdin = open('input.txt')

# 가려두면서 한 단계씩 코딩, 내가 못하는 부분 알기
def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]    # visited 생성     N+1이 아니라 N하는 건 정점번호가 아니고 미로랑 동일한 크기 만들거라서 그냥 N
    q = []                              # 큐 생성
    q.append((sti, stj))                # 시작점 인큐
    visited[sti][stj] = 1               # 시작점 인큐 표시
    # 내가 탐색할 대상만 바뀌지 위 절차는 bfs동일
    while q:                            # 큐가 비워질 때 까지
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j]-2          # 지나온 칸 수 리턴(시작점과 끝점은 빼야 하기 때문)
        # 인접하고 인큐된 적이 없으면..
        # 인큐, 인큐 표시

        for di, dj in [[0,1], [1,0], [0, -1], [-1,0]]:
            ni, nj = i+di, j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0                # 3인 칸에 도달할 수 없는 경우

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 미로를 읽는 방법, 2차원 배열 칸칸이 숫자로 넣는 방법
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)      # 시작점 찾기, 안에서 해도 되고, 밖에서 해도 된다... 뭔 솔?
    print(f'#{tc} {ans}')                            # 거리를 알아낸 다음에 알아낸 거리를





