
# greedy 하게 풀면 풀릴 것 같지 않지만, 예사치 못한 집합 만들어질 것.

# 상호 배타 집합 과정 거치면 돼. 어떤 union을 이루냐.

import sys
sys.stdin = open('input.txt')

# union 처리 -> 집합 x와 집합 y를 하나의 집합으로 연합 이루게 하기

'''
1 2 3 2
[0 1 2 3]
[0 1 1 3]  | x = 1, y = 2
[0 1 1 2] | x = 2, y = 3 
-> x,y의 루트 노드가 누구인지 (집합의 대장이 누구인지 찾는 과정)

1 2 3 2
[0 1 2 3]
[0 1 1 3]  | x = 1, y = 2
| x= 2 (2번 노드 집합의 대장을 찾아서 반환)
[0 1 1 1] | x = 1, y = 1 

'''

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 랭크 작은 녀석을 랭크 가장 높은 값에 붙여줘야 한다.
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] =y
    # 두 루트 노드의 rank가 동일하다면,
    # 어디에 누구를 붙이든 똑같으니 하나 정해서 증가시켜준다.

    if rank[x] == rank[y]:
        rank[x] += 1






# 내 조상이 누구인지 찾아가는 함수
# 루트 -> 자기 자신을 부모로 잡고 있는 노드가 될 때까지 조사.

def find_set(x):
    # x 노드의 부모가 자기 자신: 즉, x가 루트노드다.
    if parent[x] == x: # 루트 노드인 x를 반환
        return x
    else:
        return find_set(parent[x])




T =int(input())

for tc in range(1, T+1):
    # N = 총 학생 수
    # M = 투표지(간선 개수)
    N,M = map(int, input().split())

    # 인접 행렬 or 인접 리스트
    arr = list(map(int, input().split()))

    # 간선 정보를 모른다는 가정하에
    # 최초의 각 노드들 정보를 초기화

    # make set 과정 그냥 리스트 만드는걸로 끝!
    parent = list(range(N+1))
    # print(parent)
    # print(arr)

    # 각 노드가 자식 노드를 얼마나 연결하고 있는지를 초기화
    rank = [0] * (N+1)



    for i in range(M):
        x = arr[i*2]
        y = arr[i*2+1]
        union(x,y)
    print(arr) #간선 정보
    print(parent)
    print(set(parent))
    print(len(set(parent)))
    # 아무도 관심없는 0 번 노드 공집합 뺴줘야 하니
    print(len(set(parent))-1)


    # 랭크정보 기록하면서 코드 짜야 해.