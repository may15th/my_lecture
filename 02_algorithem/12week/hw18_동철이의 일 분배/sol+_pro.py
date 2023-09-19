import sys
sys.stdin = open('input.txt')

# r: 현재 조사한 원소 개수
def perm(r, acc):
    global result
    if acc <= result:
        return
    # 종료 시점
    if r == N:
        result = acc
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                perm(r+1, acc*arr[r][i])
                visited = False

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    # 각 정수 Pi => 확률
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         arr[i][j] /= 100
    visited = [0] * N
    #비교 대상군 ->0
    result = 0
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    print(arr)
    perm(0,1)