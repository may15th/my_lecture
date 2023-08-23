#최소 heap구현

N = 6
arr = [3, 6, 2, 7, 9, 1]

tree = [0] * (N+1)      # 0번은 안쓸거니까     # index 조절하면서 집어넣어 봐라
last = 1

for i in range(N):
    if tree[i] == 0:
        tree[last] = arr[i]
    else:            #이미 값이 있을때
        last += 1
        tree[last] = arr[i]
        child = last    #자식의 위치

        # 완전 이진 트리에서 부모의 위치는 자식의 위치를 2로 나누 몫
        parent = child // 2

        # 최소 힙 구현하려면 tree[p] < tree[c] 해야되니
        # while문으로 구현할거면 반대로 tree[p]>tree[child]로 해야함.
        while parent >= 1 and tree[parent] > tree[child]:
            # 부모, 자식 값 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식의 위치가 swap한 부모의 위치가 되도록 설정
            child = parent
            # 부모의 값은?
            parent = child // 2
            

    print(tree)




