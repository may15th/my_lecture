import sys
sys.stdin = open('input.txt')

def backtrack(row, n, now_sum, visited):
    global min_sum  # 최소합을 전역변수로 선언
    if row == n:  # i가 배열의 수와 일치하면      # n이 아니라 n-1 되야 하는 거 아니야?? 아 아래쪽에서 backtrack함수를 계속해ㅓ 호출하고 이게 재귀 함수 인것.
        # 현재 합과 (지금까지)최소합 값을 비교
        if now_sum < min_sum:
            min_sum = now_sum  # 현재합이 더 작으면 대체
    elif now_sum > min_sum:
        return  # 현재 부분합이 더 크면 탐색 중지 (Pruning) #그냥 return만 써줘도 되는건가??
    else:
        for col in range(n):
            if not visited[col]:  # 방문 전인 컬럼
                visited[col] = 1  # 방문처리
                #                 # 다음 row로 넘어가고, now_sum에 값을 더해주고, visited 갱신
                backtrack(row + 1, n, now_sum + num[row][col], visited)
                #num[row][col]을 col이 변할 때마다 한번씩 호출한다는 뜻...
                visited[col] = 0  # 함수 적용 후 초기화 (재검색 할 수 있도록)

T = int(input())
for tc in range(T):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 100
    # 값을 대체해주기 임의의 큰 수 대입, 이 문제에서는 min_sum = num[0][0]으로 하면 안됨
    # 답 이상하게 나온다...
    visited = [0] * n

    backtrack(0, n, 0, visited)  # 함수시작
    print(f'#{tc + 1} {min_sum}')


    # 무조건 선택 가능? 선택하면 visited표기해서 가져가지 않도록 하는 것.