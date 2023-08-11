'''
출력
#1 1
#2 0
#3 1
#4 0
#5 0
#6 1
#7 0
#8 1
#9 1
#10 0
'''


#행 i, 열j
# for i 0-> 9
# tmp= set()으로 만들고 

# for j 0-> 9
# tmp= []
# set

# 3*3영역을 어떻게 돌아다닐까?
# for i: 0->6, 3씩 건너 뛰어서
# 2중 for문으로 만들 수 있을 것.
# for i in range(0,7,3):
#   for j:
#       for p:0 -> 2
            # for q: 0->2

# for tc in range
# for i in range(9):
#     for j in range(9):
import sys
sys.stdin = open('input.txt')



# 아래 교수님 풀이 무슨 의미인지 모르겠다...
# def sudoku(arr):
#     for i in range(9):
#         cnt = [0] * 10      # [0] * 9가 되어야 할 듯?
#         for j in range(9):
#             cnt[arr[i][j]] += 1  # append는 사용 못하나?
#         for k in range(1, 10):
#             if cnt[k] == 0:  # 1~9에 빠진 숫자가 있으면
#                 return 0
#             # break  # for k return 다음에 0은 의미없음


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr) # 스도쿠가 완성되면1, 아니면0
    print(f'#{tc} {ans}')

