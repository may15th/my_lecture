import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):  # 세로 길이 (행) 길이 만큼 반복해서
        puzzle.append(input().split())  # split 안해도 상관 없습니다
    cnt = 0

    #3중 for문 + for else문을 이용한 풀이
    for i in range(N):
        for j in range(N):

            if i == 0 or puzzle[i - 1][j] == '0':  # 직전 인덱스가 검은색 블록, 범위가 넘어간 것

                # 이 코드 else if 구문이 아니라 for else구문이라함 이번 기회에 for else구문 공부하지 뭐~~
                for r in range(i, i+K): # for else 구문의 for
                    if r == N or puzzle[r][j] == '0':  # 범위를 넘어서거나 0을 만나면 X
                        break  # for r in range(i, i+K):

                else:  # for else 구문의 else 모든 for가 문제없이 동작됐을 때 아래 돌아감
                    if i+K == N or puzzle[i+K][j] == '0': # 다음 점이 검은벽. 단어가 완결되었다
                        cnt += 1

            if j == 0 or puzzle[i][j-1] == '0':  # 직전 인덱스가 검은색 블록, 범위가 넘어간 것
                # 검색을 진행.
                # 열 방향 이동 (column: 열)
                for c in range(j, j + K): # i -> j
                    # 찾으려고 하는 j번째의 인덱스부터 j+K-1까지의 인덱스 (K개) 를 검색
                    if c == N or puzzle[i][c] == '0':  # 범위를 넘어서거나 0을 만나면 X
                        # r == N은 범위 끝을 넘어갔다는 말. -> N-1
                        break  # for r in range(i, i+K):
                else:  # 문제없이 위의 k개의 빈공간이 확보되었다?
                    # 지금 현 검색하는 점의 행 위치에 K를 더한게 N -> 다음 점이 범위 밖. 단어가 완결되었다
                    if j + K == N or puzzle[i][j + K] == '0':  # 다음 점이 검은벽. 단어가 완결되었다
                        cnt += 1
    # 자리의 수를 출력한다
    print(f'#{t} {cnt}')