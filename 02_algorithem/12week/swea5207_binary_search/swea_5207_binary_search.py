import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    def binarysearch(low, high, target):

        global cnt_left
        global cnt_right

        print(cnt_left, cnt_right)

        if low > high:
            return -1

        mid = (low+high)//2

        #1. 가운데 값이 정답인 경우
        if target == A[mid]:
            return mid

        #2. 타겟이 가운데 값보다 큰 경우
        elif target > A[mid]:
            cnt_right += 1
            return binarysearch(mid+1, high, target)

        #3. 타겟이 가운데 값보다 작은 경우
        else:
            cnt_left += 1
            return binarysearch(low, mid-1, target)


    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    cnt_left, cnt_right = 0, 0

    for i in B:
        if binarysearch(0, len(A)-1, i) >= 0 and cnt_left == cnt_right:
            cnt += 1


    # print(f'#{tc} {cnt} {cnt_left} {cnt_right}')
    print(f'#{tc} {cnt}')
    # print(f'#{tc} {ans}')