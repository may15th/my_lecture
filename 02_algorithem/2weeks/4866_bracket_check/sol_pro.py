import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    op = '({'

    #최종 결과값
    result = 1
    stack = []

    for char in word:
        # if char == '(' or char == '{':
        if char in op:
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    result = 0
                    break

                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
    if stack:
        result = 0
    print(f'# {tc} {result}')

