import sys
sys.stdin = open('input (11).txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 2차원 행렬 입력 하는 코드 매우중요!!!
    matrix = [list(map(int, input().split())) for _ in range(N)]
    #입력 완료!
    # print(matrix)
    fly =[]
    #i는  N-M까지 반복
    for i in range(N-M+1):
        #j도 N-M까지 반복
        for j in range(N-M+1):
            #ci,cj는 M까지반복(파리채로 치는 x,y값)(i,j)에서 (di,dj)를 순회하면서 더해주는 아이디어
            #영역별 파리 수 총합을 저장하는 변수 초기화, 여기서 해줘야함. 그래야 순회하면서 max값 구함.
            total = 0
            for ci in range(M):
                for cj in range(M):
                    if (i+ci) in range(N) and (j+cj) in range(N):
                        total += matrix[i+ci][j+cj]

            fly.append(total)
    max_v = fly[0]
    for i in fly:
        if i > max_v:
            max_v = i
    print(f'#{tc} {max_v}')





    #         if sum > result:
    #             result = sum
    # print(f'{tc} {result}')



# 2차원 리스트 입력 받는 코드
# #1
# mylist=[0 for _ in range(n)]

# for i in range(n):
#     mylist[i]=list(map(int, input().split()))


# #2
# mylist=[]
# for i in range(n):
#     mylist.append(list(map(int, input().split())))


# #3
# mylist=[list(map(int, input().split())) for _ in range(n)]

# T = int(input())
# for tc in range(1):
#     sum = 0
#     max = 0
#     di = [0,0,1,1]
#     dj = [0,1,1,0]
#
#     N, M = map(int, input().split())
#     arr=[list(map(int, input().split())) for _ in range(N)]    #이렇게 2차원 리스트 입력한다는 걸 기억해야 함.
#
#     for i in range(0,N):
#         for j in range(0,N):
#             for k in range(4):
#                 ni,nj = i + di[k], j +dj[k]
#                 if ni > N or nj >= N:
#                     arr[ni][nj] = 0
#                 sum = arr[ni][nj]
#     print(sum)


