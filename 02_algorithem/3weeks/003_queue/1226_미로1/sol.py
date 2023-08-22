'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
아래의 예시에서는 도달 가능하다.

아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.
테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
'''
'''
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1
'''
import sys
sys.stdin = open('input.txt')

def find_start(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)] # visited 0으로 행렬 초기화
    q = []  #q 빈리스트 초기화
    q.append((sti, stj))    # 튜플로 기록할 거라서 이렇게 한 것.
    visited[sti][stj] = 1       # visited 1 표시해 줌.

    while q:        # q 빈 리스트 될때까지
        i, j = q.pop(0) # q에서 값꺼내고
        if arr[i][j] == 3:  # arr[i][j] = 3이면 도착이니까
            return 1    #bfs함수 마지막 보면 return기본값은 0인데, 도착점인 3인 지점 갈 경우 1 리턴

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:       # 이 리스트 컴프리헨션 구문 기억!
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] == 0: # N안 포함이 맞지??
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0        # 리턴의 기본값은 0인데




T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    #input().split()을 습관적으로 하는데, input()만 해야될 때 이문제 같은 경우가 있다!
    sti, stj = find_start(N)
    # print(sti, stj)       #확인용 sti, stj 정상 불러오는지.
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')