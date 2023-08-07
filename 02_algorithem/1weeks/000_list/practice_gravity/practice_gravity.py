
#import sys
#sys.stdin = open('input.txt')

#테케 입력
T = int(input())
for tc in range(1, T+1):
    # 정수 입력
    N = int(input)
    #boxes 리스트 작성
    boxes = list(map(int,input().split()))
    #최종값 작성
    result = 0
    #for문 순회하는 동안 최대값은 아래와 같고
    for i in range(N):
        max_h = N - (i+1)
        #boxes i번째 보다 겉거나 높은 값이 있다면 낙차 -1됨
        for j in range(N):
            if boxes(i) <= boxes(j):
                max_h -=1
        #i=0~8까지 max_h를 result값과 비교해서 새로운 result만들어줌
        if result >= max_h:
            result = max_h

    print(f'{tc} {result}')