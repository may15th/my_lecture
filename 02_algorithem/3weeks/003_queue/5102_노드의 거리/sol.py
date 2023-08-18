'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.

노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.
'''

'''
출력
#1 2
#2 4
#3 3
'''

import sys
sys.stdin = open('input.txt')

def check(S, G):
    visited = [0]*(V+1)     # 간선인 E가 아니라 노드 V의 갯수가 기준이 된다!!
    visited[S] = 1
    q = []
    q.append((S,0))         #이 부분이 이해가 안된네 왜 S를 넣는게 아니라 (S,0)?
    while q:
        c,num = q.pop()
        # 현재 노드에서 갈 수 있는 경로 찾기
        for i in range(1,V+1):
            if adj_m[c][i] and not visited[i]:
                # 도착했는가?
                if i == G:
                    return num +1
                q.append((i, num + 1))
                visited[i] = 1
        # 도착 못 함(S와 G가 연결되어 있지 않음)
        return 0


T = int(input())
for tc in range(1,T+1):
    # V:노드의 갯수, E: 방향성이 없는 간선
    V, E = map(int, input().split())

    # 인접행렬: 간선 연결확인
    # 노드 번호 1~V번
    adj_m = [[0]*(V+1) for _ in range(V+1)]

    # E개의 간선의 양쪽 노드 번호
    for _ in range(E):
        i, j = map(int, input().split())
        # 양쪽 다 표시
        adj_m[i][j] = 1
        adj_m[j][i] = 1

    # 출발 노드, 도착 노드
    S, G = map(int, input(). split())

    # 최소 이동 간선 개수
    result = check(S, G)