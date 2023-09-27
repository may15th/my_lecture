import math

'''
4
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
1 1 1 1 1 1

1
0 0 13 40 0 37
'''

T = int(input())
for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    d = int(d)

    print(d)

    if x1 ==x2 and y1==y2 and r1==r2:
        ans = -1


    elif max(r1, r2) < d:
        if r1+r2 > d:
            ans = 2

            # print(1, ans)

        if r1 + r2 == d:
            ans = 1

            # print(2, ans)

        if r1 + r2 < d:
            ans = 0

        # print(3, ans)



        # print(4, ans)

    elif max(r1, r2) > d:
        if abs(r1 - r2) > d:
            ans = 0

            # print(5, ans)

        if abs(r1 - r2) == d:
            ans = 1
            # print(6, ans)

        if abs(r1 - r2) < d:
            ans = 2

            # print(7, ans)

    print(ans)

    # print('=========')

