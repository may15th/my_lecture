import sys
sys.stdin = open('input.txt')

T = int(input())

def palindrome(arr):
    k = len(arr)//2
    cnt = 0
    for i in range(k):
        if arr[i] == arr[N-i-1]:
            cnt += 1
            if cnt == k:
                return arr



for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for j in range(M)]
    if arr[i] == arr[N-1-i]:

