'''
 SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
가장 좌상단에 있는 칸 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때,
 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
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

def find_start():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j  #튜플일 필요 없이 바로 i,j 보낸다

def bfs(sti, stj):   #시작 좌표와 N을 보낸다
    visited = [[0]*16 for _ in range(16)]   # visited 행렬 0으로 초기화
    queue = []      #빈 큐 생성
    queue.append((sti, stj))   # queue 초깃값 append #sti, stj를 튜플로 큐에 입력함을 기억!!
    visited[sti][stj] = 1

    while queue: #큐가 빈 리스트가 될때까지
        i, j = queue.pop(0)  #일단 첫 번째 들어있는 요소 pop
        if arr[i][j] == 3:
            return 1            #arr[i][j]가 3이라면 도착 한 것이므로 1출력 하고 종료

        # for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))   # queue는 ni,nj가 튜플로 저장되고
                visited[ni][nj] = 1     # visited행렬 ni,nj는 1 방문표시
    return 0        # 리턴의 기본값은0 인데

T = 10
# tc는 매번 입력해줘야 함
for _ in range(1, T+1):
    tc = int(input())
    # input이 띄워쓰기 없이 이루어짐.
    arr = [list(map(int, input())) for _ in range(16)]
    # sti, stj 구하는 방법 잘 보자. find_start 구조와 더불어.
    # sti, stj를 구한 후 아래 bfs함수의 인자로 넣는다
    # find_start는 아무것도 인자로 받지 않는다.
    sti, stj = find_start()
    #bfs는 sti, stj, N을 인자로 받는다
    ans = bfs(sti, stj)
    print(f'#{tc} {ans}')


# 보충할 점 N=16으로 놓고 다시 풀어보기