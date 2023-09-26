'''
2
-5 1 12 1
7
1 1 8
-3 -1 1
2 2 2
5 5 1
-4 5 1
12 1 1
12 1 2
-5 1 5 1
1
0 0 2

'''
'''
3
-5 1 5 1
3
0 0 2
-6 1 2
6 2 2
2 3 13 2
8
-3 -1 1
2 2 3
2 3 1
0 1 7
-4 5 1
12 1 1
12 1 2
12 1 3
102 16 19 -108
12
-107 175 135
-38 -115 42
140 23 70
148 -2 39
-198 -49 89
172 -151 39
-179 -52 43
148 42 150
176 0 10
153 68 120
-56 109 16
-187 -174 8

'''

T = int(input())
# print('테케갯수', T)

for tc in range(1, T+1):
    se = list(map(int, input().split()))
    n = int(input())
    ans = 0

    # print('시작점끝점',se)
    # print('행성수', n)


    for _ in range(n):
        planet = list(map(int,input().split()))
        # print('행성좌표', planet)

    #1 행성계가 시작점 끝점 둘다 포함하지 않는다 +0
    #2 행성계가 시작점 끝점 둘다 포함한다
    #3 행성계가 시작점만 포함한다 +1
    #4 행성계가 끝점만 포함한다 +1

    #1
        # print('행성', (planet[0]))
        # print('시작점 x', se[0])
        # print('시작점 y', se[1])
        # print('끝점 x', se[2])
        # print('끝점 y', se[3])
        dist_s_square = (planet[0]-se[0])**2 +(planet[1]-se[1])**2
        dist_e_square = (planet[0]-se[2])**2 +(planet[1]-se[3])**2
        r_square = planet[2]**2
        # print('시작점 거리', dist_s_square)
        # print('끝점 거리', dist_s_square)
        # print('행성계 제곱', r_square)




        if dist_s_square < r_square:
            ans +=1

        if dist_e_square < r_square:
            ans +=1

        if dist_s_square < r_square and dist_e_square < r_square:
            ans -= 2
        
    print(ans)