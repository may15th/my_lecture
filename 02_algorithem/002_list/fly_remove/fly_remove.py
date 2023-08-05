# import sys
# sys.stdin = open('input (11).txt')



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
for tc in range(1):
    sum = 0
    max = 0
    di = [0,0,1,1]
    dj = [0,1,1,0]

    N, M = map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]    #이렇게 2차원 리스트 입력한다는 걸 기억해야 함.

    for i in range(0,N):
        for j in range(0,N):
            for k in range(4):
                ni,nj = i + di[k], j +dj[k]
                if ni > N or nj >= N:
                    arr[ni][nj] = 0
                sum = arr[ni][nj]
    print(sum)


            