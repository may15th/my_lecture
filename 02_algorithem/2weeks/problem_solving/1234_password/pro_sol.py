# 리스트 만들고 왼쪽에 있는 값들과 비교. 같은 값이 있다면 삭제
# 같으면 소거
# 다음 값은 지워진 애들 빼고 그 앞에 값을 봄.

# 0. 스택이 비어있거나 pop과 다르면 peek != tmp 둘다 push(tmp)
# 1. stack을 만든다 스택 비어있으니 1푸쉬.
# 2. 스택이 비어 있지 않거나 top과 같으면 pop


###pass word가 가장 쉬워보인다 이것부터 하자.

# 3. 다 지운 거니까 남아있는 수들 들어 있으면,
# 4. top은 pop하나씩 지우면서 1씩 지우고 해야함.
import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):
    str_N, str_num = input().split()
    # print(str_N, str_num)

    N = int(str_N)
    #스택 만들어야
    stack = [0] * N     # stack = []으로 빈스택을 만들면 안됐나?
    top = -1

    #str_num을 가져올건데 하나씩 가져오기로 할지 인덱스로 접근할 지 결정.
    for t in str_num: #(str_N범위가N길이정보로 주어졌으니 이 방법 장려)
        if top == -1 or stack[top] != t:        # 스택이 비어있거나, stack의 top원소와 다르면
            top += 1
            stack[top] = t
        # 예전 문제들 에서는 top = -1로 썼었던 것 같은데, 여기서는 왜 -1인거지?
        else:
            top -= 1

        # 출력 문자열 리스트에서 값들 붙이는 법1
        # ans = ''
        # for i in range(top+1):
        #     ans += stack[i]
        # print(f'#{tc} {ans}')



        # 출력 문자열 리스트에서 값들 붙이는 법2
    ans = ''.join(stack[:top+1])
    print(f'# {tc} {ans}')