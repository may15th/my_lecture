# 가능한 모든 경우 실행
# 가장 좋은 방법은 tree로 펼쳐서 보는 게 가장 좋은 형태이다.

# 길이 M짜리 수열을 만드는 것.

# 재귀 형태로 그린다.

# 백트래킹은 dfs로 연계된다?

# 백트래킹 가능한 모든 경우 실행하기 때문에 무조건 정답이 나온다!

# 종료조건, 하부함수 호출 두 가지만 생각.

### dfs 함수 짜여짐.
# dfs(n, lst)
# if n==M; #종료
# ans.append(lst)
# return

# for j in (1,N+1)
# if v[j] ==0;
#     v[j] = 1
# dfs(n+1,lst+[j])
# v[j] = 0

# 중복확인용

def dfs(n,lst):
    # 종료조건(n에 관련)처리+정답처리



import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
ans = [] # 정답 리스트를 저장할 리스트
v = [0] * (N+1) # 중복을 확인할 visited[]

dfs(0, [])
for lst in ans:
    print(*lst)


