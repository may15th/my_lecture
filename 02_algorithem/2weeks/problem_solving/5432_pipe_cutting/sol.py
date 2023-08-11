# 레이저가 자른 쇠막대 갯수는 쌓여
# 끝나면 조각이 닫혔을때 +1 됨
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pipe_lazor = input()

    # 궁금한 건 이렇게 해도 i+1바로 찾아가나?
    for i in pipe_lazor:
        if i == '(':
            if i+1 == ')':
                pipe_lazor[i] = 'L'
                pipe_lazor[i+1] = ''

    for j in range

    cnt = 0
    ans = 0
    stack = []