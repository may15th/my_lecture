#기본 아이이디어
# bubble_sort로 오름차순 정렬 후에
# boxes[-1]-1 boxes[0]+1
# 다시 오름차순 정렬
# 위 3단계 dump횟수 만큼 반복
# import sys
# sys.stdin = open('input (10).txt')

for tc in range(1, 11): #테케 갯수
    dump = int(input()) #dump 횟수
    boxes = list(map(int, input().split())) #boxes 높이 리스트
    N = 10 #boxes 가로길이는 100고정

    # bubble_sort(boxes, N)
    # do_dump(boxes)

    def bubble_sort(arr, n): #정렬할 list, n의 원소 수
        for i in range(n-1, 0, -1):
            for j in range(i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
                return boxes
    print(bubble_sort(boxes, N))

    def do_dump(arr):
        arr[-1] = arr[-1] - 1
        arr[0] = arr[0] + 1
        bubble_sort(boxes, N)
        result = arr[-1] - arr[0]
        return result


    # print(f'#{tc} {result}')