#
# N = int(input())
# arr = []
# for _ in range(N):
#     n = int(input())
#     arr.append(n)
#
# def bubble_sort(arr):
#
#     for i in range(N-1, 0, -1):
#         for j in range(0, i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     result = arr
#     return result
#
# for i in bubble_sort(arr):
#     print(i)

#2587 대표값2
# arr = []
# sum_v = 0
# for _ in range(5):
#     n = int(input())
#     arr.append(n)
#
# for i in arr:
#     sum_v += i
#
# def bubble_sort(arr):
#     for i in range(4, 0, -1):
#         for j in range(0, i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     result = arr
#     return result
#
# avg = sum_v//5
# print(avg)
# bubble_sort(arr)
# print(arr[2])

#커트라인
# N, k = map(int, input().split())
# x = list(map(int, input().split()))
# x.sort()
# print(x[N-k])

#1427 소트인사이드

# n = int(input())
#
# li = []
# for i in str(n):
#     li.append(int(i))
#
# li.sort(reverse=True)
#
# for i in li:
#     print(i, end='')

N = int(input())

