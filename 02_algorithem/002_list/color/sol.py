import sys
sys.stdin = open('input.txt')

#테스트 케이스 입력
T=int(input())

for tc in range(1, T+1):
    # 색칠할 갯수
    N = int(input())
    # tc마다 10*10행렬 초기화
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    # 색칠 N번 시행
    result = 0

    for _ in range(N):
      r1, c1, r2, c2, color = map(int,input().split())
      for i in range(r1, r2+1):
         for j in range(c1 ,c2+1):
            matrix[i][j] += color
            if matrix[i][j] == 3:
               result += 1

    print(f'#{tc} {result}')


