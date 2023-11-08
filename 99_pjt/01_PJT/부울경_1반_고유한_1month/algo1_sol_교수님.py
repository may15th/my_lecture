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

