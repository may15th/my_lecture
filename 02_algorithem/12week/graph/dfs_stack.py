# 인접 행렬
# 갈 수 있다면 1 갈수 없다면 0을 모두 가짐.
# 장점 : 사용이 굉장히 편하다. 구현이 쉬움.
# 단점 : 메모리 낭비, 0도 표시를 하기 때문에
arr = [
    [0,1,0,1,0]
    [1,0,1,1,1]
    [0,1,0,0,0]
    [1,1,0,0,1]
    [0,1,0,1,0]
    ]

# DFS
# STACK 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue
            
# 백트래킹 등으로 들어갈 때 조건이 많을 때 반복이나 재귀만들 때 할 수 없는 경우를 
# pass 조건은 continue로 넣는다. -> 확실히 이 방법이 다른 문제들에서도 자주 사용.
# !!!!꿀팁이다 꼭 기억하고 활용하자!!!
# 일종의 가지치기로 쓰는 것!
            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited

print("dfs_stack = ", end='')
print(*dfs_stack(0))


# 재귀 버전