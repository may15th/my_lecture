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
'''
input

4 2
'''
'''
output
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
'''
# 이걸 왜 스택으로 푸는 거지?

def dfs(n, lst):
    # 종료조건(n에 관련) 처리 +정답 처리
    if n == M: #M개의 수열을 완성
        ans.append(lst)
        return

    #하부(단계) 함수 호출
    for j in range(1, N+1):
        if v[j] == 0: # 선택하지 않은 숫자인 겨웅 추구ㅏ
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

N, M = map(int, input().split())
ans = []
v = [0] * (N+1)
dfs(0,[])


print(ans)

for lst in ans:
    print(*lst)




