# 테스트 케이스 갯수 입력
T = int(input())
# 테스트 케이스 순회
for tc in range(1, T+1):
    # 정사각행렬의 행, 열 수 N 입력
    N = int(input())
    # 평탄화 영역 좌표값 입력
    r1, c1, r2, c2 = map(int, input().split())
    # 배열값 입력
    arr = [list(map(int, input().split())) for _ in range(N)]


    # r1~c2까지 입력, 배열입력을 반대로 해서 틀림. 이런 사소한 실수들 주의해야 한다.

    #평균값 구하기 위한 sum값, cnt값 0으로 초기화
    sum = 0
    cnt = 0
    # 행은 r1부터 r2까지, 열은 c1부터 c2까지 순회
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            # 순회하면서 sum값에 arr[i][j]를 누적합, cnt 1씩 더해줌.
            sum += arr[i][j]
            cnt += 1
    # 평균값
    avg_v = sum//cnt
    # 평탄화 값 grounding = 0으로 초기화
    grounding = 0
    # 평탄화 값 구하기 위해 각 요소값들 avg_v를 빼줌.
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            # grounding에 평탄화 값들 누적합
            if arr[i][j] >= avg_v:
                grounding += (arr[i][j] - avg_v)
            else:
                grounding += (avg_v - arr[i][j])

    # 평탄화 값 출력
    print(f'#{tc} {grounding}')