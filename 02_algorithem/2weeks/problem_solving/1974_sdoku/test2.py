import sys
sys.stdin = open('input.txt')

# 0으로 값 채운 리스트 만들고, 값 대입 후 각 요소들에 값 더해가면서 2개라면 return 0 아이디어....


def sudoku_checking(arr):
    #행 검사
    for i in range(9):
        # 행리스트 초기화
        lst_h = [0] * 10
        # 열리스트 초기화
        lst_v = [0] * 10
        for j in range(9):
            lst_h[arr[i][j]] += 1
            if lst_h[arr[i][j]] == 2:
                return 0

    #열 검사
            lst_v[arr[j][i]] += 1
            if lst_v[arr[j][i]] == 2:
                return 0

    #3*3스도쿠 검사
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            lst_3 = [0]*10
            for i in range(3):
                for j in range(3):
                    lst_3[arr[x+i][y+j]] += 1
                    if lst_3[arr[x+i][y+j]] == 2:
                        return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'{tc} {sudoku_checking(arr)}')
