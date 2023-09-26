from itertools import combinations
'''
3
2 2
1 5
13 29

'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 1
    N_factol = 1
    for i in range(M,M-N,-1):
        ans *=i

    for j in range(N,0,-1):
        N_factol *= j
    # print(ans)
    # print(N_factol)
    ans = ans//N_factol
    print(ans)