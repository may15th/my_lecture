'''
10
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''
# 총 9개 행 리스트 뽑기
arr = [list(map(int, input().split())) for _ in range(9)]
print(arr[0]) # 행 출력만 가능함을 알 수 있다.
print(set(arr[0]))
for i in range(9):
    print(arr[i])
print('=================')

# 스도쿠 9작은 정사각형 리스트 뽑기
for k in range(0, 7, 3):
    for l in range(0, 7, 3):
        list_ = []
        for i in range(3):
            for j in range(3):
                list_.append(arr[i+k][j+l])
        print(list_)


print('=================')

# 전치행렬한후 행리스트 비교하면 열 비교가능한거랑 같음
# 총 9개 열 리스트 뽑기
for i in range(9):
    for j in range(9):
        arr[i][j] = arr[j][i]

# set으로 비교 함수 만들기
def sudoku_checking(arr, list_):
    check_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return 1
    for i in range(9):
        if set(arr[i]) != check_set:
            return 0
            break
    for i in range(9):
        if set(list_[i]) != check_set:
            return 0
            break
print(sudoku_checking(arr, list_))
