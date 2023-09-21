

# heapq 가능? heapq로도 구현 가능한데 sort()로. 정렬되면 정렬된 순서대로 쓰면 됌.


# prim 알고리즘
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 모든 간선들 중 비용 가장 적은 것 우선적으로 고르자
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w를 기준으로 정렬
edge.sort(key=lambda x: x[2])   # 코테에서 람다함수로 구현 속도 천차만별 되는 경우 있으니 람다 함수도 꼭 암기
                                # edge list의 2번 인덱스 값 기준으로 정렬. 즉, w를 기준으로 정렬한다.

# 간선 선택시 사이클 발생 여부를 확인해야 함.
# 사이클 발생 여부를 unino find로 해결

parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    
    else:
        parents[x] = y

# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    #싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면      
        if cnt == V:
            break
print(f'최소비용 = {sum_weight}')


# 디버깅 툴도 연습해야해. 내일 문제 풀이하면서 봐준다고 함.
# 코드 올려주면 그거 비교해서 추가 공부해야 함.
