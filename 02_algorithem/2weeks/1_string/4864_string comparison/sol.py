import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    target = input()
    m = len(pattern)
    n = len(target)

    result = 0
    target3 = ''
    for i in range(0, n-m+1):
        if target[i] == pattern[0]:
            target2 = ''
            for j in range(1, m):
                target2 += target[i+j]
            target3 = target[i] + target2
        if target3 == pattern:
            result = 1

    print(f'#{tc} {result}')

