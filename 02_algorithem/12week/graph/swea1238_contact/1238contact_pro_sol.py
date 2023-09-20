import sys
sys.stdin = open('input.txt')



# 마지막으로 연락 받은 대상의 번호를 출력
    # 마지막으로 연락 받은 사람이 여러명이면, 가장 출석 번호가 높은 학생을 반환

def BFS(s):
    q = [s, 0]
    # s: 탐색 시작 노드
    # cnt: 현재 노드까지 도달하는데 걸린 시간
    visited[s] = 1
    while q:
        s, cnt = q.pop(0)
        #현재 조사 대상 s노드가 진출차수가 없다면 빈 리스트 반환 -> 순회 안함
        for i in G.get(s, []):
            if not visited[i]:
                # i번쨰 방문하는 데 거린 시간
                visited[i] = cnt + 1
                q.append((i, cnt + 1))
        #마지막으로 반환된 게, 마지막 조사 대상일 것.

for tc in range(1,11):
    N,S = map(int, input().split())
    arr = list(map(int, input().split()))

    # N//2 개의 간선이 있다.

    # stack으로 못푸는 건 아니지만 queue로 풀어야 한다.

    # 한 번이라도 방문 안하면 방문하지 않도록 visited[] 만들 것.

    # 학생은 1번부터 100번까지 있다.
    # 0번은 없겠지만, 간선 정보에 각 학생 번호를 index로 쓰려면.... 이쪽이 편하다.
    visited = [0] * 101
    # 인접 행렬 or 인접 리스트 필요
    G = {}
    # 전체 연락망 정보 개수 //2 -> 간선 개수
    # 방향성 있는 그래프
    for i in range(N//2):
        # 딕셔너리로 간선정보 만들기
        # G.get(1, []) : G 키가 1인 값이 없으면 빈 리스트 반환
        # G.get(1, []) + [2] -> G = [1:2]
        G[arr[i*2]] = G.get(arr[i*2],[]) + [arr[i*2+1]]
        last = BFS(s)

        # 마지막에 도착한 친구와 동일한 시간이 걸림
        # visited에 걸린 시간 기록해둔 갑싱 같은 노드들만 출력
        # 출석번호가 가장 높은 대상을 출력하고 종료

        for i in range(100, -1, -1):
            if visited[i] == visited[last]:
                print(f'#{tc} {i}')
                break
        print()
