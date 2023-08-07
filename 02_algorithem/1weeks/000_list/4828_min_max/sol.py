import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    numbers = list(map(int, input().split()))
    max_v = numbers[0]
    min_v = numbers[0]

    
    for number in numbers:
        ## number가 0번째일땐 굳이 할 필요 없기 때문
        if number == 0:
            continue
        if number > max_v:
            max_v = number
        if number < min_v:
            min_v = number

    result = max_v - min_v
    print(f'#{tc} {result}')