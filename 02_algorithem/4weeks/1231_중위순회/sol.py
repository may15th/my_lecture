#중위 순회
import sys
sys.stdin = open('input.txt')

def inorder(a):
    if a <= N:
        inorder(a*2)
        print(alp_li[a], end = '')
        inorder(a*2+1)

# 테케 10으로 주어짐
for tc in range(1,11):
    # N = 트리가 가지는 정점 수
    N = int(input())
    #
    alp_li = [0] * (N+1)
    for i in range(N):
        li = list(input().split())
        alp_li[i+1] = li[1]

    print(f'#{tc}', end = ' ')
    inorder(1)
    print()