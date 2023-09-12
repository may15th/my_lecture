# 스택 사용한 풀이
# 와 계산기는 진짜 하나도 모르겠다....ㅠㅠㅠㅠㅠㅠㅠ
import sys
sys.stdin = open('input.txt')

pri = {'*' : 2, '+' : 1}
T = 10
for tc in range(1, T+1):
    N = int(input())
    st = input()

    equ = ''
    stk = []

    # [1] 중위 - > 후위표기식
    for ch in st:
        if ch.isdigit():        # 숫자일 경우 isdigit()은 숫자일 경우 조건식으로 자주 사용하니 기억
            equ += ch

        else:
            if not stk:
                stk.append(ch)
            else:
                if pri[ch] > pri[stk[-1]]:
                    stk.append(ch)          # if든 else든 append 해준다.
                else:
                    while stk and pri[ch] <= pri[stk[-1]]:
                        equ += stk.pop()    # if든 else든 append 해준다.

                    stk.append(ch)

    while stk:
        equ += stk.pop()


    # [2] 후위 연산식 계산
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if ch == '*':
                stk.append(op1*op2)
            elif ch == '+':
                stk.append(op1+op2)

    print(f'#{tc} {stk.pop()}')


    print(f'{tc} ')