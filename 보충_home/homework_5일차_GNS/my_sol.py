import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(1, T+1):
    tc, cnt = input().split()

    arr = list(input().split())     # 왜 list(map(input().split()))은 안되는가
    # print(arr)
    cnt = int(cnt)
    arr2 = []

    com_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in com_lst:
        # print(com_lst)
        for j in range(cnt):
            if arr[j] == i:
                # print(arr[j])
                arr2.append(arr[j])
    print(tc)
    print(' '.join(arr2))

# arr3 = [1,2,3,4,5,6]
# arr4 = []
# for i in range(6):
#     arr4.append(arr3[i])
#
# print(arr4)
