import sys
sys.stdin = open('input (10).txt')

for tc in range(1, 11): #테케 갯수
    dump = int(input()) #dump 횟수
    boxes = list(map(int, input().split())) #boxes 높이 리스트
    N = 100 #boxes 가로길이는 100고정

    

#     def bubble_sort(arr, n): #정렬할 list, n의 원소 수
#         for i in range(n-1, 0, -1):
#             for j in range(i):
#                 if boxes[j] > boxes[j+1]:
#                     boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
#         return arr            #이 result문도 return 위치 잘못잡았었따.. for문 바깥으로!! 했었네... 주의!!!
#     # print(bubble_sort(boxes, N))

#     def do_dump(arr):
#         bubble_sort(arr, N)
#         arr[-1] -= 1
#         arr[0] += 1
#         bubble_sort(arr, N)
#         result = arr[-1] - arr[0]
#         return result

#     # print(result) #이거 왜 안돼?
#     print(do_dump(boxes))
    

#     # print(f'#{tc} {result}')

#     for tc in range(1, 11): #테케 갯수
#     dump = int(input()) #dump 횟수
#     boxes = list(map(int, input().split())) #boxes 높이 리스트
#     N = 9 #boxes 가로길이는 100고정

    

    # def bubble_sort(arr, n): #정렬할 list, n의 원소 수
    #     for i in range(n-1, 0, -1):
    #         for j in range(i):
    #             if boxes[j] > boxes[j+1]:
    #                 boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
    #     return arr            #이 result문도 return 위치 잘못잡았었따.. for문 바깥으로!! 했었네... 주의!!!
    # # print(bubble_sort(boxes, N))

    # 더 간단한 코드가 있을텐데...ㅋㅋ
    # 일단 bubble 함수까지 do_dump함수 안에 넣고 해서 풀었는데
    # bubble함수, do_dump함수 따로 풀 수 있는지 알아보자...
    # global변수 안쓰면 do_dump함수안에서는 정의 안되서 못 쓴다..ㅋㅋㅋ 이것도 알게 된 사실 주의하자!


    def do_dump(arr):           
        global dump
        dump2 = dump
        while dump2:
            for i in range(N-1, 0, -1):
                for j in range(i):
                    if boxes[j] > boxes[j+1]:
                        boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
            arr[-1] -= 1
            arr[0] += 1
            for i in range(N-1, 0, -1):
                for j in range(i):
                    if boxes[j] > boxes[j+1]:
                        boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
            result = arr[-1] - arr[0]
            dump2 -= 1
        return result

    # print(result) #이거 왜 안돼?
    print(f'#{tc} {do_dump(boxes)}')