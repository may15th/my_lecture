#테스트 케이스 입력받음
T = int(input())
for tc in range(1,T+1):
    #n*n행렬 n입력
    n = int(input())
    
    #length = n 
    def make_outer(arr, start, length, num):
        last = start+length-1 # 사각형:(start,start)~(last,last)
        for c in range(start, last+1): #해당 최외각 사각형에서 첫째 행 처리
            arr[start][c] = num
            num += 1
        for r in range(start+1, last +1):
            arr[r][last] = num
            num+=1
        for c in range(last-1, start-1,-1):
            arr[last][c] = num
            num += 1
        for r in range(last-1,start,-1):
            arr[r][start] = num
            num+=1
        return num

    arr = [[0 for j in range(n)] for i in range(n)]
    num, start = 1,0
    while n > 0:
        num = make_outer(arr, start, n, num)
        n -=2
        start +=1

    print(f'#{tc}')
    for row in arr:
        print(*row)


#c = 열, r = 행



#delta 탐색 이용
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# x +=dx[i]
# y +=dy[i]

# 빈 리스트 모두 0으로 채움

# 빈 리스트 인가? 0으로 찬 리스트인가? 
# 조건1) 을 범위를 벗어나지 않는 동안으로 지정 
# 조건2) 리스트에 숫자가 들어있을 경우? or 0보다 큰 숫자면 우회하도록
# 나는 4,,4,4 ,3,3,2,2,1,1로 할려 했는데


##dx,dy = [][] 상하좌우 이동하도록 넣고


###달팽이 델타탐색 고급 버전,
## 내일 EXTRA 델타탐색이 더 쉬울 수도