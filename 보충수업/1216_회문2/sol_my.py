# import sys
# sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(3)]
    print(arr)
    for i in range(3):
        for j in range(3):
            for m in range(3,0,-1):
                print(arr[i][j:m])
                print(arr[i][j:m][::-1])
                if arr[i][:m] == arr[i][:m][::-1]:

    arr = list(zip(*arr))
    print(arr)



'''
1
AAB
BCB
CCB
'''