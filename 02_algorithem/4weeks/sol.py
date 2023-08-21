import sys
sys.stdin = open('input.txt')


V = int(input())
E = V - 1
edge = list(map(int, input().split()))

print(edge)

