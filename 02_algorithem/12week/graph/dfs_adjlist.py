# 인접리스트
# 갈 수 있는 지점만 체크. 불필요한 0없어 메모리 절약 가능
#dfs를 이용한 stack(작은번호 부터 출력)
# 주의사항
    # => 각 노드마다 갈 수 있는 지점의 개수가 다름
    # # => range 쓸 때 index 조심
# 메모리가 인접 행렬에 비해 훨씬 효율적이다.abs
# 코딩 테스트, 개발에서는 행렬보다 리스트에 익숙해지는 게 좋아.


graph = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]
arr[0][1]

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

        # for next in range(5)
        # 작은 번호부터 조회
        for next in range(len(graph[now])-1,-1,-1):
            # 이제 연결이 안 되어 있다는 건 애초에 저장하지 않았으므로
            # 체크할 필요 없음
            # if graph[now][next] == 0:
            #     continue

            # 방문한 지점이라면 stack 추가하지 않음.
            if next in visited:
                continue

            stack.append(next)
    return visited

print("dfs_stack = ", end='')
print(*dfs_stack(0))