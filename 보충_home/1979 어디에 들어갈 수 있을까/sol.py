'''
이거 그냥 while문으로 조건 주는 게 훨씬 좋을 것 같은데;;;


'''


T= int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 한 행에 값이 1인 칸 갯수 세어줌
    cnt = 0
    # K와 일치하는 행 또는 열의 수
    ans = 0

    # i,j 순회하면서
    for i in range(N):
        for j in range(N):
            # arr[i][j] 가 1이라면 cnt 값 더해주고(나중에 비교_
            if arr[i][j] == 1:
                cnt += 1
            # arr[i][j]가 0인 순간 그동안 누적한 cnt값이 K랑 일치하는지 확인
            if arr[i][j] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0


    print(f'#{tc} {ans}')
    
    # 열우선 탐색, 하고 전치행렬까지 해보기
    for i in range(N):
        for j in range(N):
            

    # 전치행렬 변환
    #for i in range(N):
     #   for j in range(N):
      #      arr[i][j] = arr[j][i]

    #print(arr)

'''
1
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''