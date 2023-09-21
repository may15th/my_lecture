import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    # print(nums)

    def quick_sort(arr,left, right):

        if left < right:
            mid = cal(arr,left, right)
            quick_sort(arr, left, mid -1)
            quick_sort(arr, mid+1, right)

    def cal(arr, left, right):

        i = left - 1
        j = left
        pivot = arr[right]
        while j< right:
            if pivot >arr[j]:
                i+=1
                if i<j:
                    arr[i],arr[j] = arr[j],arr[i]
                    # print(arr)
            j+=1
        arr[i+1], arr[right] = arr[right], arr[i+1]
        # print(left, right)
        # print(arr)
        return i+1

    #nums의 시작값,끝값을 각각 left,right로 quick_sort 함수 호출
    quick_sort(nums, 0, len(nums) - 1)
    ans = nums[N//2]
    print(f'#{tc} {ans}')

'''
output
#1 2
#2 6
'''