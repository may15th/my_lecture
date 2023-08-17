import sys
sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    cnt = 1
    # data의 끝 값이 0이면 종료
    while data[-1] > 0: # 0보다 큰 동안 순회
        if cnt >= 6:         #이 while아래 if 문이 빼는 값이 1~5로 순회하는 for문 역할을 한다!!!
            cnt = 1
        tmp = data.pop(0) - cnt
        data.append(tmp)
        cnt += 1
    print(cnt)

    data[-1] = 0

    print(f'{tc}')
    print(*data)