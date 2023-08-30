import sys
sys.stdin = open('input.txt')

def recur(cur, start, total):
    global min_total
    if cur == n-1:  # 마지막에 사무실을 갈 때 사용량을 더한다.
        min_total = min(min_total, arr[start][0] + total)
        return
    for i in range(1,n):    # 사무실로 가면 안되니 1부터
        if visited[i] == 0 and start != i:
            visited[i] = 1
            recur(cur+1, total + arr[start][i])
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]     # 방문표시
    min_total = 1001
    recur(0,0,0)
    print(f'#{tc} {min_total}')