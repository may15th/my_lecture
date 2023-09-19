# import sys
# sys.stdin = open('input.txt')


def permutation(r, acc):
    global result
    if acc > result:
        return

    # 종료 시점
    if r == N:
        if acc > result:
            result = acc
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                # 1번 인부의 1번 제품 생산 확률을 ACC에 누적
                permutation(r+1, acc*arr[r][i])
                # 1번 인부 1번 제품 안만들고, 2번 제품 만들때
                visited[i] = False

T = int(input())
for tc in range(1, T+1):
    # 배열의 길이
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr[][] 사용여부
    visited = [0] * N
    #비교 대상군
    result = sum(sum(arr,[]))   #이중 리스트의 모든 값을 더해줌.
    permutation(0,1)
    print(result)

'''
INPUT
1
3
13 0 50
12 70 90
25 60 100
'''

'''
OUTPUT
#1 9.100000
'''