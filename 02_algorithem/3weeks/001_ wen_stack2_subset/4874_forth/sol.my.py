import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    forth = list(map(str, input().split()))
    stack = []
    error = False       #에러 기본값 False설정. 이후

    for i in range(len(forth)-1):
        # 피연산자(숫자)인지 확인 후 stack에 더해줌
        if forth[i].isdigit():
            stack.append(forth[i])

        else:
            try:
                # stack에서 값 하나씩 빼서 사칙연산 수행
                b = int(stack.pop())
                a = int(stack.pop())

                if forth[i] == '+':
                    c = a+b
                elif forth[i] == '-':
                    c = a-b
                elif forth[i] == '*':
                    c = a*b
                elif forth[i] == '/':
                    c = a//b    # 실제로 나머지 버리니까 '/'가 아니라 '//'로 설정해야 함.

                stack.append(c)

            # 연산자도, 피연산자도 아닌 값이 forth중에 있다면 i순호하면서 검출, error 트루 뜸.
            except:
                error = True

    # 모든 연산 마친후 error가 true이거나, stack에 남은 값이 1이 아니라면 error 출력
    if error == True or len(stack) != 1:
        result = 'error'
    else:
        result = stack.pop()

    print(f'#{tc} {result}')



