# 테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):

    # 입력 값 입력, 괄호 검사를 위한 리스트, stack은 빈 리스트로 초기화, 리스트의 인덱스 알려주는 top = -1로 초기화
    arr = list(map(str, input()))
    stack = []
    top = -1

    # result 기본값은 1로 초기화
    result = 1

    for char in arr:
        if char != ')' and char != '}':
            stack.append(char)
        if char not in ')}':
            stack.append(char)

        else:
            if char == ')':
                tmp = 0
                # stack에 값이 있는 동안
                while stack:
                    # val 정수일때
                    if val.isdigit():
                        tmp += int(val)
                        val = stack.pop()
                        # 값 누적
                    elif val == '(':
                        #누적된 값을 stack에 추가
                        stack.append(str(tmp))
                    elif val == ')':
                        # 조사 멈춤
                        break

                    # val '(' dlfEo

                    pass




            elif char == '}':
                pass
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

# 특정상황일 때 실행하는 쉬운 방법 = 함수를 사용하락 함.
# search 함수를 실행시키고 결과값을 잠깐 빼온다??
# list index out of range stack이 비어있을 때도 아예 stack자체가 비어있을때도 실패하는 것 그때도 -1해줘야.
# 진짜 어려운 문제였네... 이거 교수님 풀이보고 꼭 풀어봐야 함..!!!!

'''
3
(2{(58)7}43)
(2{(58}7)43)
2{(58)7}43
'''
