def quick_sort(arr, left, right):
    # 분할 정복이 핵심
    # 정복 대상의 범위를 가장 작아질 때까지 쪼갠다.

    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)

# lomuto => 피봇을 가장 오른쪽 원소로 결정
# j가 이동하면서 피봇값보다 큰값일ㅋ때만 i +=1 해주고
# j는 한 칸씩 이동하니까 무조건 j +=1
def cal(arr, left, right):
    # i :피봇보다 큰 구간의 왼쪽경계 나타냄
    i = left - 1
    # j : 피본보다 큰 구간의 오른 쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        # 피봇이 j번째 값보다 더 크면
        if pivot >arr[j]:
            i +=1
            # i와 j사이 구간에 피봇보다 큰 값이 있다.
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
                print(arr)
        j += 1
    arr[i+1], arr[right] = arr[right], arr[i+1]
    print(left, right)
    print(arr)
    return i+1

nums = [23,12,60,77,32,1]
print(nums)
# pivot은 어디로 두든 상관 없다. 왼, 오로 쪼갠다는게 중요
quick_sort(nums, 0,len(nums) -1)