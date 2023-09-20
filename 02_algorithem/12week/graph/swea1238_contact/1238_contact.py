# import sys
# sys.stdin = open('input.txt')
'''
input
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''

'''
output
#1 17
'''

T = 10
for tc in range(1, T + 1):
    l, s = map(int, input().split())
    arr = list(map(int, input().split()))

    p,c = [],[]



    for i in range(l):
        if i % 2 == 0:
            p.append(arr[i])
        else:
            c.append(arr[i])

    print(p)
    print(c)

    for j in range(len(p)):
        union(p[j],cj)
