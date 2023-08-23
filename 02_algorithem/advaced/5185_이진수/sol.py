import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, N16 = input().split()
    for char in N16:
        print(char)
