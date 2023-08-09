import sys
sys.stdin = open('input.txt')


for _ in range(4):
    stack = []
    sentence = input()

    '''
    ()()((()))
    ((()(((()()((()())((())))))
    (())(((())()))(()()((()))
    ))))
    '''
    result = 1
    for i in sentence:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                result = -1
            else:
                stack.pop()

    if stack != []:
        result = -1

    print(result)

    # print(stack)




## 밑으로 내려보쇼


# 함수를 정의해놓고 그걸 안쓰는 이유는??
# if stack 이면 stack이 비어있지 않다는 뜻인데,
# 그러면 짝 안맞으니까 0 출력해야함(안맞는경우를 0이라고 하고싶다면)
# print(result) 인덴트 안맞음, 현재상태면 비어있지 않은 경우에만 result 출력
# 인덴트를 맞추면 result가 미리 선언되어 있지 않기 때문에 에러뜰거임
# 그럼 result를 미리 정해줘야겠지?



