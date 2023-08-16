'''

Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
3 4 + .
Forth에서는 동작은 다음과 같다.

숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
다음은 Forth 연산의 예이다.

코드
출력
4 2 / .
2
4 3 - .
1

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

입력
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .


출력
#1 84
#2 error
#3 168

'''
import sys
sys.stdin = open('input.txt')


# 테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):
    forth = list(map(str, input().split()))
    stack = []      #후위표현식 계산을 위한 스택
    error = False

    #마지막 .빼고 for문 넣기(어차피 .은 맨마지막이라 -1한 것.)
    for i in range(len(forth) - 1):
        if forth[i].isdigit():  # 숫자라면 스택에 더하고, (.isdigt() 메서드 기억)
            stack.append(forth[i])

        # 연산자면 숫자 두개 빼서 계산
        else:
            # 에러 처리를 위한 try 문
            try:
                # 숫자 2개씩 뽑기(숫자 2개씩 뽑아서 바로 뒤에 연산자로 계산)
                # 스택 위에 있는 게 나중 값이라서 b를 먼저 pop해줌 기억.
                b = int(stack.pop())
                a = int(stack.pop())
                # 연산자에 따라 계산(4칙연산 if문으로 하나씩 정의해줌)
                if forth[i] == '+':
                    c = a + b
                elif forth[i] == '-':
                    c = a - b
                elif forth[i] == '*':
                    c = a * b
                elif forth[i] == '/':
                    # 나멎는 버려야 하니까 '//' 연산자 활용
                    c = a//b

                stack.append(c)

            except: # 숫자도 연산자도 아니면 에러
                error = True

    # 에러가 True이거나 스택에 남는 게 하나가 아니라면 error출력( len(stack) !=1일 때도 error 뜨는 건 이해가 안되네)
    if error == True or len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')
