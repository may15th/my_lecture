# 뭔가 잘못되서 코드 작동 안되는데... 다시 코드 확인하기!

def bfs(start):
    #bfs 어떻게 쓸 까
    # 갈 수 있는 것들 큐에 넣고
    # 큐에 있는 값 뺴고 다시 넣고... 반복

    q = [s]
    visited = [0] * 101
    # 시작점은 방문 처리
    visited[s] = 1

    # 최대 숫자오 최대 깊이를 저장할 변수
    max_number = s
    max_depth = 1
 
    while q:
        now = q.pop(0)
        
        # 갈 수 있는 지점 다 봐라.
        for to in graph[now]:
            if visited[to]:
                continue

            # 두번 째 방문한 지점이 2번, 3번 이라는 건 어떻게 저장할까?
            # -> visited[] 를 원래 0,1로 표현했다면. 기존 visited 보다 한번 더 갔다! 로 생각
            visited[to] = visited[now] +1

            # 가장 나중에 연락 받게 되는 사람 중 번호가 가장 큰 사람 구하는 함수
            # 최대 visited보다 크면, 이라는 조건. 최대 visited가 어딘가에 저장되어야 함
            # max_number, max_depth 변수 사용

            # 한 단계 더 깊은 곳으로 가거나
            # 깊이는 같은데, 숫자가 더 크다면
            # max값을 초기화
            if max_depth <visited[to] or (max_depth == bisited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to

            q.append(to)

    return max_number




for tc in range(1, 11):
    n, start = map(int, input().split())
    # 임시로 전체 입력을 받음
    input_graph = list(map(int, input().split()))
    
    #실제 사용할 인접 리스트 -> input_graph를 사용해서 만든다.
    graph = [[] for _ in range(101)]    #range 범위 왜 101? 
    # 인접행렬, 인접 리스트 만들 때에는 나올 수 있는 n값의 범위 연락인원이 1이상 100이하라고 했으니까, 10로
    # 대신에 인접 행렬일 경우 [101][101] 이면 10000개정도 메모리 낭비가 생기니, 인접 리스트로 만드는 것.
    for i in range(0,n,2):
        f = input_graph[i]
        t = input_graph[i+1]
        graph[f].append(t)
    r = bfs(start)
    print(f'#{tc} {r}')

    
