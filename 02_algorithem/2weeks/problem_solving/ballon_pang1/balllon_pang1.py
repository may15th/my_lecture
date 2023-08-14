'''
종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고,
어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.
예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면
상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램을 만드시오.
(3<=N, M<=100)

입력
첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

출력
#과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0

###arr[i][j]+1만큼 순회해서 더해줘야 하는 게 point

    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for dir in range(4):
                for k in range(1, arr[i][j]+1):
                    ni = i + di[dir]*k
                    nj = j + dj[dir]*k
                    if 0 <= ni <= (N-1) and 0 <= nj <= (M-1):
                        sum += arr[ni][nj]

            if max_v < sum:
                max_v = sum

    print(f'#{tc} {max_v}')





