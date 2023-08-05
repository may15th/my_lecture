# 1209 sum


'''
#input
1
13 24 13
14 14 28
26 13 6

'''

T = int(input())

for tc in range(1,T+1):
    sum1 = 0 #좌상 -> 우하
    sum2 = 0 #우상 -> 좌하
    sum_row_list = []
    sum_col_list = []
    max = 0
    max_list = []

    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    for i in range(N):
        sum1 += arr[i][i]   #1.좌상 -> 우하 대각선 합
        sum2 += arr[N-i-1][i]   #2. 우상 -> 좌하 대각선의 합
        sum_row = 0 #각 행의 합         #초기화 위치도 중요... 초기화 코드 돌아가면 어떻게 되지 머릿속으로 돌려보는 것 중요
        sum_col = 0 #각 열의 합
        for j in range(N):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        sum_row_list.append(sum_row)
        sum_col_list.append(sum_col)

    # print(sum_row_list)
    # print(sum_col_list)

    max_list = [sum1, sum2] +sum_row_list + sum_col_list
    ### 여기서 느낀 점은 maxlist.append(sum1,sum2,sum_row_list,sum_col_list) 하면 될 줄 알았는데, 안되서 당황, extend도 똑같이 안되서 당황... append, extend 잘 아시는 분 설명좀...
    # print(max_list)
    for i in max_list:
        if i > max:
            max = i
    
    print(f'#{tc} {max}')     
        
            






        # for j in range(N):
        #     s = arr[i][j]   
            
            
            
        #     for p in range(1, 100):
        #         for k in range(8):
        #             ni,nj = i +di[k], j +dj[k]
        #             if 0 <= ni <N and 0<= nj <N:
                    