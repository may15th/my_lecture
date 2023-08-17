import sys
sys.stdin =open('input.txt')

#deque()정의 하는 순간 회색에서 색깔 나오는 걸로 활성화된다. 기억
from collections import deque

T = 10
for tc in range(1, T+1):
    n = int(input())

    queue = deque(list(map(int, input().split())))

    while queue[-1] > 0:
        for i in range(1, 6):
            queue[0] -= i
            # tmp = queue.pop(0)            데크는 pop(0) 팝에 요소 못넣음. popleft로 빼기!
            tmp = queue.popleft()
            queue.append(tmp)

            if queue[-1] <= 0:
                break

    queue[-1] = 0

    print(f'#{tc}', end = ' ')        #1출력 방법1   둘중하나 주석처리해야 함.
    for i in queue:
        print(i, end = ' ')
    print('')

    print(f'{tc}', *queue)          #2출력 방법2
    # 좀 더 예쁜 식이 있을 듯...
    # queue 언패킹 하면 된는구나 ㅋㅋㅋㅋ

    # print(f'#{tc} {queue}')