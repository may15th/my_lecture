# BFS 문제!!!
# 최단거리를 찾는 문제가 아니기 때문에 DFS로도 풀이 가능하다 함.
# 코드 간단하지만 동작이 느리다. 최단거리 찾으려면 보다 복잡한 중복 방문 처리가 필요하다.
# 목적지까지 도달하는 경로의 수가 몇개냐? 이런 문제가 나온다면 DFS로 가능한 방향으로 다가면 경로가 생긴 것.
# 그래서 위 같은 문제에는 DFS로 푼다. DFS가 코드는 간단하다고 함.


T = 10
for _ in range(1,11):
    tc = int(input())
    n = 16
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 조건 네 방향/ 미방문/ 벽이 아니면 !=1 인경우 방문하면 됨.
    # q.append, visited[]에표시 1/0

