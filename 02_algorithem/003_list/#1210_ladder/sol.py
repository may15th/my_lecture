import sys
sys.stdin = open('input (10).txt')
# 아이디어는 사다리 0~99열 전체 탐색
# 델타 탐색 하, 좌, 우 순으로 탐색

#델타 탐색에서 하, 좌, 우 순으로 탐색하기 위함
di = [1, 0, 0]
dj = [0, -1, 1]

#필요인자 : 시작 좌표(x,y)
def search(x,y):
    # 각 시작 좌표들마다 방문 표시를 위한 2차원 리스트

    # 만약 2를 찾았을 때, 반환해야 할 시작 좌표 y를 기록
    original_y = y
    print(x, y, '여기 맞니?')
    #(1) 조사조건은 x가 99가 되기 전까지.
    while x !=99:
        print(x, y,'왜 99가 안되니?')
        for k in range(3):
            ni = x +di[k]
            nj = y +dj[k]

            #조건문 걸어서 행렬 초과 안 할 경우만 잡는다.
            if  0<= ni< 100 and 0<=nj <100 and data[ni][nj]:
                x, y = nx, ny

    #x가 99 된 순간
    if data[x][y] == 2:
        return original_y
    else:
        return '실패'




T = int(input())
for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)] #100*100행렬 초기화

    #모든 출발점 찾기
    for i in range(100):
        #항상 0번째 열에서 출발
        #0번째 열의 i번째 행의 값이 1이면
        if data[0][i] == 1:
            result = search(0, i)
        if result != '실패':
            break
    print(f'#{tc} {result}')

