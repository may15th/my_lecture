T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # root를 1로 한다
    # tree를 그릴때, 0번은 쓰지 않는다
    # N 노드의 갯수
    # tree N+1개 만큼 담을 수 있어야 한다.

    tree = [0] * (N+1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
