# 계산기2에서 ()가 포함된 형태
#1 []가 있는 중위표기식을 후위표기식으로 변형
import sys
sys.stdin = open('input.txt')

# in coming priority는 딕셔너리로 준다.
# in stack priority도 딕셔너리로, 근데 우선순위를 주는 건...
icp = {'(':3, '*':2, '+':1}
isp = {       '*':2, '+':1, '(':0}

T = 10

for tc in range(1, T+1):
    _ = input()
    st = input()        # st = string

    equ = ''
    stk = []

    # [1] 중위표기식 -> 후위표기식
    for ch in st:
        if ch.isdigit():
            equ += ch
        else:
            if ch == ')':
                while stk:      #꺼낼때는 항상 stack check해야.
                    t = stk.pop()
                    if t == '(':
                        break
                    else:
                        equ += t

            else:       #연산자
                while stk and icp[ch] <= isp[stk[-1]]:
                    equ += stk.pop()
                stk.append(ch)
    while stk:
        equ +=stk.pop()
    # 위 코드로 후위표기식으로 변환 완료

    # [2] 후위표기식 계산
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()     # op1, op2 순서에 주의!!
            op1 = stk.pop()
            if ch == '*':
                stk.append(op1*op2)
            elif ch == '+':
                stk.append(op1+op2)

    print(f'#{tc} ')

    print(f'#{tc} {stk.pop()}')