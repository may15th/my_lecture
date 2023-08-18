'''
#1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''


def bfs(s, V):               # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)   # visited 생성 # 마지막 정점 번호 인덱스까지 만들기 위해 +1 해줌.
    q = []                  # 큐 생성
    q.append(s)             # 시작 점 인큐
    visited[s] = 1          # 시작점 방문 표시     위 4단계가 기본작업
    while q:                # 큐에 정점이 남아있으면 front != rear 
        t = q.pop(0)        # 디큐
        print(t)            # 방문한 정점에서 할 일
        # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
        # w인큐, 인큐되었음을 표시(i라고 표시해도됨)
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1     # 이거는 의미가?? 아 그냥 visited 0에서 1찍는단 의미




V, E = map(int, input().split())        # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접 리스트 ================================
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(1, 7)

# 오류 뜬다 ㅋㅋㅋㅋㅋ GPT도 이상없는 코드라는데...
