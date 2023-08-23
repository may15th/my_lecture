import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    arr2 = [0] * len(arr)
    cnt = 0

    for i in range(len(arr)):
        if arr2[i] != arr[i]:
            cnt += 1
            for j in range(i, len(arr)):
                arr2[j] = arr[i]

    print(f'#{tc} {cnt}')



'''
1
1010
'''

    #
    # print(cnt)
    # print(arr)
    # print(arr2)
    # print('===========')
    # pirnt(f'#{tc} {ans}')