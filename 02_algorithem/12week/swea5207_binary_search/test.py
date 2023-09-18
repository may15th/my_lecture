def binarysearch(low, high, target):
    if low > high:
        return -1

    mid = (low+high)//2

    #1. 가운데 값이 정답인 경우
    if target == A[mid]:
        return mid

    #2. 타겟이 가운데 값보다 큰 경우
    elif target > A[mid]:
        return binarysearch(mid+1, high, target)

    #3. 타겟이 가운데 값보다 작은 경우
    else:
        return binarysearch(low, mid-1, target)



A = [1,3,5,7,9]
target = 1

print(binarysearch(0,len(A)-1,1))
