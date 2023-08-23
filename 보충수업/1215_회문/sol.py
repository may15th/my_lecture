import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    mat = [list(map(str,input())) for _ in range(8)]
    print(mat)


    print(f'#{tc} {}')