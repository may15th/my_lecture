import sys
sys.stdin = open('input.txt')

def preorder(node):
    if node !=0:                # 왼쪽 자식이 있을때만 돌 수 있도록...
        print(node, end = ' ')
        preorder(tree[node][0])
        preorder(tree[node][1])
        preorder(left[node])
        preorder(right[node])


#중위순회 LVR
def inorder(node):
    if node != 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])

# 후위순회 LVR  LRV 아닌가?
def postorder(node):





V = int(input())
E = V - 1
edge = list(map(int, input().split()))

# 왼쪽 자식, 오른쪽 자식, 부모정보
left = [0] * (V+1)
right = [0] * (V+1)
parent = [0] * (V+1)
# [왼쪽, 오른쪽, 부모]
tree = [[0]*3 for _ in range(V+1)]
print(tree)


# 간선 정보 전수 조사
for i in range(E):
    p, c = edge[i*2], edge[i*2 + 1]
    if left[p] == 0:        # 아직 왼쪽 자식이 기록되지 않았다면
        left[p] = c
    else:
        right[p] = c
    parent[c] = p

    if tree[p][0] == 0:
        tree[p][0] = c

    else:
        tree[p][1] = c
    tree[c][2] = p

print(tree)

root = 0
for i in range(1, V +1):
    if parent[i] == 0:
        root = i
        break
print(root)




print(edge)
print(left)
print(right)
print(parent)

print('---전위순회-----')
preorder()
print('-----중위순회-----')
inorder(root)
print('-----후위순회----')
postorder(root)