#테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):

    #정사각행렬의 행,렬 값 N입력
    N = int(input())
    # 행렬 요소값 입력
    arr = [(list(map(int, input().split()))) for _ in range(N)]
    # 우,하,좌,상 델타탐색을 위한 값 입력
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 봉우리 갯수를 세기 위한 cnt 변수 0으로 초기화
    cnt = 0

    # i,j를 순회하면서
    for i in range(N):
        for j in range(N):

            # dir 0~3 순회하면서 우,하,좌,상 인덱스 값 구하기
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]

                # 행렬 범위 지정 ni, nj는 0~N-1 까지만, 행렬범위 내 순회
                if 0 <= ni <= N-1 and 0 <= nj <= N-1:

                    # 만약 모든 arr[ni][nj]보다 arr[i][j]가 크다면
                    # cnt 갯수 추가
                    if arr[i][j] > arr[ni][nj]:
                        cnt += 1

    print(f'#{tc} {cnt}')
