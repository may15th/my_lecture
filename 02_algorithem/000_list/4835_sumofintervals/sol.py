import sys

T = int(input())
N,M = map(int,input().split())
numbers = list(map(int,input().split()))

#테케 입력
for tc in range(1, T+1):
    max_v=min_v=0
    #각 테스트케이스마다 결과값은 0 초기화
    result = 0
    #0번째부터 N-M-1요소가 더하는 수의 0번째 인덱스
    for i in range(N-M+1):
        #구간합은 0으로 초기화
        sum_of_interval = 0
        for j in range(i, i+M):         
            sum_of_interval += numbers[j]
        
        if sum_of_interval > max_v:
            max_v = sum_of_interval
        if sum_of_interval <min_v:
            min_v = sum_of_interval

    result = max_v - min_v
    print(f'#{tc} {result} ')


    