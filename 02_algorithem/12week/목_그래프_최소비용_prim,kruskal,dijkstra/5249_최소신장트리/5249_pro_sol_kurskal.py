# 최소 신장트리라기보다는...

import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x== root[x]:
        return x
    else:
        return find_set(root[x])


def mst():
    cnt = 0     # 모든 간선에 대해 조사가 되었느냐 조사하는
    result = 0  # 전체 가중치의 합
    idx = 0     # 조사 대상

    while cnt < V: # 조사한 간선의 개수가 총 노드수보다 작은 동안, 사이클 없는 간선의 갯수는 노드의 갯수 -1
        x = find_set(arr[idx][0])   # 전출노드
        y = find_set(arr[idx][1])   # 전입노드

        # 사이클이 형성되지 않을 때 
        if x != y:
            result += arr[idx][2]
            cnt += 1
            root[y] = x     # union(x,y)에서 parent 바꿔주는 거랑 비슷한 건가?
        idx +=1 # 다음 조사 대상 이동

for tc in range(1, T+1):
    V,E = map(int, input().split())
    arr = [list(map(int, input().split()) for _ in range(E))]
    # 사이클을 모두 제거한 뒤,
    # 가중치 기준으로 오름차순 정렬되어 있느 정보를 토대로
    # 그냥 이어주기
    arr.sort(key=lambda x:x[2])
    #본인을 루트로 가지는 노드 형태라고 초기화
    root =list(range(V+1))
    print(mst())

print(arr)
arr.sort(key=lambda x:x[2])
print(arr)