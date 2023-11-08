# 테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):

    # 입력 값 입력, 괄호 검사를 위한 리스트, stack은 빈 리스트로 초기화, 리스트의 인덱스 알려주는 top = -1로 초기화
    arr = list(map(str, input()))
    open_list = ['(', '{']
    close_list = [')', '}']
    stack = []
    top = -1

    # result 기본값은 1로 초기화
    result = 1

    # str 문자열로 이루어진 arr리스트를 순회하면서
    for char in arr:
        # 만약 char이 (,{을 포함한다면 stack에 char을 push
        if char in open_list:
            stack.append(char)
            top += 1

        # 만약 char이 ) 일때
        elif char == ')':
            # stack이 비어있거나, stack 끝값이 '('아니라면 -1결과값 내고 종료
            if not stack or stack[-1] != '(':
                result == -1
                break

            # stack이 비어있지 않다면 stack 요소를 pop하고 top를 하나 빼줌.
            else:
                stack.pop()
                top -= 1

        # 만약 char이 '}' 일때
        elif char == '}':
            # stack이 비어있거나(underflow), stack 끝값이 '{'아니라면 -1로 결과값 내고 종료
            if not stack or stack[-1] != '{':
                result == -1
                break

            # stack이 비어있지 않다면 stack 요소를 pop하고 top를 하나 빼줌.
            else:
                stack.pop()
                top -= 1



    # stack이 빈 리스트가 아니라면 괄호 짝이 맞지 않는다는 의미이므로
    if stack:
        result = -1

    print(f'#{tc} {result}')


'''
3
(2{(58)7}43)
(2{(58}7)43)
2{(58)7}43
'''
