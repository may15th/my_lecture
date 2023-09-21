import sys
sys.stdin = open('input.txt')

# nPr
# r : 사용중인 원소의 갯수, 공자의 인덱스 A,B,C
# acc : 현재 경우의 수 까지 누적된 값

def permutation(r, acc):
    global result
    if acc > result:
        return

    # 종료 시점
    if r == N:
        if acc < result:
            # 모든 공장 순회 다 했고,
            # 각 공장의 비용을 다 더했는데
            # 비교 대상보다 acc값 작으면
            result = acc
        return
    else:
        # 모든 공장이 하나씩은 만들어야 하니 전수조사
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                # A공장의 1번 제품 생산비용을 acc에 누적 해본다음
                permutation(r+1, acc+arr[r][i])
                # A공장이 1번 제품을 안쓰고, 2번 제품을 썼을 때
                visited[i] = False

T= int(input())
for tc in range(1, T+1):
    # 배열의 길이
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr[?][i] 사용여부
    visited = [0] * N
    #비교 대상군
    result = sum(sum(arr,[]))
    permutation(0,0)
    print(result)


# 이건 실제로 돌려보면 시간초과 난다고 함.

# 전기버스 2 훨씬 쉬워.

# 과제 동철이의 일 분배
# 최소생산비용이라 차이없고, 프루닝 어떻게 해야 할지만 고려.!!

# permutation이랑 combination 값 출력되는 과정, 함수 return후 어디로 돌아가는지
# 만 잘 알면 좋을듯.