#전략
#1. 버블정렬로 오름차순 정렬 하나의 리스트 만듦
#2. 정렬된 리스트의 index n,0,n-1,1,n-2,2 ...이어나감
#3 #2가 안될경우 오름차순 딱 n/2인덱스 잘라서 2번 리스트에서 n,n-1,,, 1번 리스트에서 0,1,2,,, 교대로 뽑아온다.

#테케 갯수, 테케 입력
T= int(input())
for tc in range(T):
    # N 스페셜 정렬할 요소 갯수
    N = int(input())
    numbers = list(map(int,input().split()))
    
    #버블정렬로 오름차순 정렬
    def bubble_sort(arr):
        for i in range(len(arr - 1, 0, -1)):
            for j in range(i):
                if arr[j] >arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    bubble_sort(numbers)