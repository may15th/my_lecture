T= int(input())

for tc in range(1,T+1):
    N = int(input())
    Aij = [list(map(int, input().split())) for _ in range(N)]

    result = 0  #최종 결과값
    max_v = 0
    min_v = 20*20*20        # 모든 칸의 값들 다 더한 것보다는 작을 것. 2중 for문으로 다 더해더 되고
                            # 문제 조건에서 n<20 이고 aij<20이니깐

    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    #4중 for문 일때 이게 맞나? 라는 생각이 들 수도 있는데.. 맞다 ㅋㅋㅋㅋ

    for i in range(N):
        for j in range(N):
            # 좌표 i, j에 대한 조사 시작
            acc = Aij[i][j]
            for dir in range(4):
                for k in range(1, Aij[i][j] + 1):

    print('f#{tc} {result}')

