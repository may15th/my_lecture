'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
'''
'''
출력
#1 731
#2 18641
#3 2412
'''
'''
test
1
3 10
5527 731 31274
'''
#데크 사용 안해도 되는건가???

import sys
sys.stdin = open('input.txt')

#테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for i in range(M):
        tmp = queue.pop(0)
        queue.append(tmp)

    result = queue.pop(0)

    print(f'#{tc} {result}')


    # while문과 for문의 차이점
    #
    # # while M >= 0:
    #     M -= 1
    # while은 변수 값들을 바꿔가면서 대입시키면서 할려면 while
    # while문은 종료시점을 조건문으로 물어볼 것이기 때문
    #
    # for i in range(M):
    #     pass
    # print(f'{tc}')
    #