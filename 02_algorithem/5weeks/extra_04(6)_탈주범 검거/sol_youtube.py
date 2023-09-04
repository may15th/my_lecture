# 중복방문 x
# bfs:a방향, 범위 내 조건 맞으면 q 삽입
# ci, cj 지점 우측방향에....!
# ci, cj의 우측 파이프 존재 and ni, nj 좌측 파이프

# 코드에서 뭔가 잘못해서 실행이 안되는데 찬찬히 탐구해 보자...

import sys
sys.stdin = open('input.txt')

# 상,하,좌,우
p = [[0,0,0,0],
     [1,1,1,1],
     [1,1,0,0],
     [0,0,1,1],
     [1,0,0,1],
     [0,1,0,1],
     [0,1,1,0],
     [1,0,1,0]
     ]

opp = [1,0,3,2]
di, dj = [-1,1,0,0],[0,0,-1,1]

def bfs(si,sj):
    q = []
    v = [[0]*M for _ in range(N)]
    ans = 0

    q.append((si,sj))
    v[si][sj] = 1
    ans += 1
    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return ans

        # 4방향, 범위 내, 조건(현위치 - 이동할 위치 모두 파이프 있는 경우)에 맞으면
        for dr in range(4):
            ni,nj = ci+di[dr], cj+dj[dr]
            if 0 <= ni < N and 0<=nj<M and v[ni][nj] == 0 and
                p[arr[ci][cj]][dr]==1 and p[arr[ni][nj]][opp[dr]] == 1
                q. append((ni,nj))
                v[ni][nj] = v[ci][cj] +1
                ans += 1

    return ans      # 가능한 위치보다 더 긴 시간을 준 경우



T = int(input())
for tc in range(1, T+1):
    N,M,R,C,L = [list(map(int, input().split())) for _ in range()]

    ans = bfs(R,C)
    print(f'#{tc} {ans}')



























# # 현재 위치 파이프 dr 방향 값 == 1
# p[arr[ci][cj]][dr] == 1 and p[arr[ni][nj]][]
#         #현재 위치 파이프 번호
# P[arr[ni][nj]][opp[dr]]
#         # 편리하게 풀 수 있는 방법은 look up 테이블 하나 만들면 됨.
# opp = [1,0,3,2] # 내 파이프의 우측을 보면 상대방의 좌측 보인다. opp는 반대 oppsite 의미
#
# ni<N nj < M
# #언제 까지 BFS돌려야 하나. 꺼낸 날짜 == L 이면 종료 return ans








