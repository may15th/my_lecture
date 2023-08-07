#테스트 케이스 수 입력
T = int(input())
#테스트 케이스는 1~T번까지
for tc in range(1,T+1):
    #가로 수 N 입력
    N = int(input())
    # building 높이 리스트로 입력
    buildings = list(map(int,input().split()))
    
    result = 0
    #최종구할 값 view 입력 각 tc마다 구해야 하므로 tc문 안 for i문 밖
    view = 0
    #구해야 하는 빌딩은 2부터 n-2까지 순회
    for i in range(2,N-1):
        #view 수는 i 순회할 때마다 누적합이므로 for i 문 안에 
        view += view
        #view 수 구하기 위해 i-2~i+2번째 중 i번째 제외 가장 높은 값 구함
        for j in range(i-2, i+3):
            if j == i:
                continue
            if buildings[j] > max_h:
                max_h = buildings[j]

        
        if buildings[i] > max_h:
            view = buildings[i] - max_h
    print('f#{tc} {view}')