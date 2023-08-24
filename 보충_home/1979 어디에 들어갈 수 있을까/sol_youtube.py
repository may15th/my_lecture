import sys
sys.stdin = open('input.txt')

def count(arr):
    ret = 0
    for lst in arr:
        cnt = 0
        for j in range(len(lst)):
            if lst[j]: # 값이 0이 아닌 경우
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(map(list, zip(*arr)))

    # 한 행에 값이 1인 칸 갯수 세어줌
    cnt = 0
    # K와 일치하는 행 또는 열의 수
    ans = count(arr) + count(arr_t)
