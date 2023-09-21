# 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나
# 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조

# 전체 데이터 수
N = 4
# 내가 삽입해야 할 값
data = [10,15,100,1]

# 힙 구성을 위한 트리
# 전체 데이터 개수 + 1 만큼의 길이
# 이진 트리 계산 편의를 위해 0번 노드는 안쓸거니까
heap = [0] *(N+1)
# 트리에 삽입할 노드 번호
last = 1

# 최소 힙을 그린다.
# 데이터 전부 삽입
for i in range(N):
    heap[last] = data[i]
    
    # 새로 추가된 값을 자식으로 보고
    child = last
    # 부모 위치 초기화 하고
    parent = child // 2

    # 부모가 가진 값이 내가 가진 값보다 작아야함.
    # 부모가 있을때까지.
    while parent > 1 and heap[parent] >heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parentparent = child // 2
    print(heap, data[i])
    last += 1

print(heap)

