T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 행, 열 우선탐색하며 빈 칸 세어주는 변수
    cnt = 0
    # k와 일치하는 빈 칸 덩어리 세어주는 변수
    ans = 0

    # 행 우선 탐색
    for i in range(N):
        for j in range(N):
            # arr[i][j]이면 cnt갯수를 1씩 늘려준다
            # cnt >3일경우 cnt 초기화 작업 필요
            if arr[i][j] == 1:
                cnt +=1
                if cnt == K:
                    ans += 1
                    # 마지막 열까지 탐색하면서
                    if j <= N-2:
                        # 다음 열도 탐색해서 1이라면 cnt가 k+1이 되므로 더해줬던 ans를 빼준다
                        if arr[i][j+1] == 1:
                            ans -= 1

            # arr[i][j]가 0이면 cnt 초기화 시켜줌.
            if arr[i][j] == 0:
                cnt = 0
        # 행이 바뀔때마다 cnt = 0으로 바꿔준다
        cnt = 0

    # 열 우선 탐색
    # 전치 행렬 만들 때 아래 방법은 사용할 수 없다.
    # for i in range(N):
    #     for j in range(N):
    #         arr[j][i] = arr[i][j]
    # 이렇게 할 경우 값이 덮어써져 버림 예를들어 순회하면서 먼저 0,1값을 1,0값으로 바꾼후
    # 1,0을 0,1로 바꿔야 하는데 이때 0,1값은 이전에 이미 1,0값으로 바뀐 0,1값임 그래서
    # 반드시 arr2라는 새로운 행렬 만든 후 이 값 [[0]*N]*N으로 초기화 시킨 후 여기에 넣어줘야 한다




    arr2 =[[0 for i in range(N)] for j in range(N)]
    print(arr2)

    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[j][i]

    print(arr2)

    print(ans)




'''
1
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1    
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        arr[j][i] = matrix[i][j]

print(arr)

