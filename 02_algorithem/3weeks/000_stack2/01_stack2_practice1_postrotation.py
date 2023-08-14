cal = '2+3*4/5'
stack =[]
# 최조 결괏값
result =''
# 연산자 모아둘 stack

# 연산자일 경우 스택에 넣어둘 것.

# 전수조사
for char in cal:
    # 연산자라면
    if char in '+-*/()':
        # print(char, '연산자')
        # 연산자 우선 순위에 맞춰서 stack 넣거나 빼거나******이게 중요
        # 우선 순위가 높은 순으로 조건문 처리!!! 가 합리적
        if char == '(':
            stack.append(char) #우선순위 가장 높으므로 그냥 push
        
        elif char in '*/':      #나와 우선순위 같은 */ 만나면 그 *나/ pop해서 result에 붙이고 나는 stack에 붙는다.
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)

            pass

        elif char in '+-':              #위 *,/ 같은원리
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)

            pass
        elif char == ')':               #닫는 괄호 만나면 stack 요소를 한번 더 뺀다!!! 다른 것들과 다름. 그 이유는 stack제일 아래 있는 여는괄호 '('와 매칭돼야 하기 때문.
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            
            pass
    else:
        #정수면 result에 더해버리면 된다.
        result += char
    print(result, stack)        
    
            # 닫는 괄호가 가장 우선순위가 낮겠지234*5/+
            # 피연산자를 stack에 순서대로 쌓다가 계산하면 되고...
            # 어렵게 생각할 필요없이 반복문, 조건문만 잘쓰면되고

            # 연습문제 풀이 차분히 읽어보면서 줄글써봐라 설명해봐라 설명
            # 논리 로직을 생각해라.