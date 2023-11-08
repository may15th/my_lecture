T=int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # arr = input().split()
    # print(arr)      # 이렇게만 해도 자동으로 리스트로 바뀌네..!

    data = input().split()
    arr = []
    result = 0
    queue = []
    stack = []

    #
    for idx in range(N):
        if data[idx].isdigit():
            arr.append(int(data[idx]))
        else:
            arr.append(data[idx])

    # print(arr)        #프린트해서 디버깅하는 것도 실력이다 이것도 주의깊게 보자.
    bonus = 0

    for idx in range(N):
        if data[idx] == '+':
            bonus += 1
        else:
            data[idx] += bonus
            # B, C에 홀짝 판별해서 더하기
            if data[idx] % 2 == 0:   # 짝수
                queue.append(data[idx])
            else:                   # 홀수
                stack.append(data[idx])

    print(stack, queue)

    ####여기까지 b,c에 값 넣는 것###################

    ####여기부터 b,c에서 값 빼는 것##########
    for i in range(M):  # M번의 차례가 올때까지 누적 계산
        if stack:
            tmp1 = stack.pop()

        if queue:
            tmp2 = queue.pop(0)

        if i + 1 == M:
            tmp1 = stack.pop()
            tmp2 = queue.pop(0)

            print(tmp1, tmp2)
            print(stack, queue)

            result += stack.pop()
            result == queue.pop(0)

    result = 0

    for i in range(M):
        if stack:
            result += stack.pop()
        if queue:
            result += queue.pop(0)

    print(f'#{tc} {result}')



    # # 데이터 입력시 리스트 컴프리헨션도 좋음 한줄로
    # data = list(map(lambda x : int(x) if x.isdigit() else x, input().split()))
    # 풀어쓰기