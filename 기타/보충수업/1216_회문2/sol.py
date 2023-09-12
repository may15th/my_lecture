import sys
sys.stdin = open('input.txt')


def palindrome(M,arr):
    for i in range(100):
        for j in range(100-M+1):
            if arr[i][j] == arr[i][j+M-1]:




T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    # M 회문의 길이
    for M in range(100,-1,-1):   #이게 포인트네...
        if palindrome(M, arr):
            print(f'{tc} {M}')
            break






