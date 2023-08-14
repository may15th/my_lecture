# 2 + 3 *4 / 5

cal = '2+3*4/5'
# 최종결괏값 쌓아나갈 빈 문자열

result = '' # 피연산자 +연산자

# 연산자들을 뫄 둘 stack이 필요해
stack = []

#전수조사
for char in cal:
    # 연산자가 아닌 경우 (정수인 경우)
    if char not in '+-*/':
        result += char
    else:
        stack.append(char)
# stack에 들어있는 모든 연산자들을 result에 더해주려면
while stack:
    result += stack.pop
print(result, stack)
# 근데 이렇게 만든건 후위 푝법 규칙도 안맞으니... 올바ㅡㄴ 건 01번 참조.