import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    # 분할

    if len(arr) < 1:
        return arr
    else:
        # 분할 작업
        pivot = arr[0]
        left, right = [], []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
            return [*quick_sort(left), pivot, *quick_sort(right)]


T = int(input())

# 파이써닉이 시간초과 많이 나는 이유
# 나와 같은 크기의 값을 left에 집어넣어
