import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 우리는 각 피자의 번호가 필요하닺!!!!! 이거 생각해 내는 게 포인트 인덱스, 치즈양을 동시에 가지는 리스트 등 새로운 객체를 만드는
    # 아이디어 생각하는 게 포인트!!
    # enumerate 뭐더라?? ㅋㅋㅋㅋㅋㅋㅋ

    Ci = [[idx, val] for idx, val in enumerate(list(map(int, input().split())), 1)]
    queue = []

    # 첫

    for i in range(N):
        queue.append(Ci.pop(0))

    # 오븐에 피자가 하나 남을 때까지.
    while len(queue) > 1:       # 화덕에 피자가 2개 이상 있는 동안
        pizza = queue.pop(0)
        # pizza의 0번 : 피자 번호
        # pizza의 1번 : 치즈 양

        #치즈를 절반 녹여서 재할당
        pizza[1] //= 2
        if pizza[1] > 0:        # 아직 치즈가 남았다면
            queue.append(pizza)

        # 아직 피자가 남았는데, 오븐에 빈 공간이 있다면(queue 리스트에 담겨있는 요소ㅢ 수가, 최대 크기보다 작다면)
        if Ci and len(queue) != N:
            #남은 피재 빼서 화덕에 넣기
            queue.append(Ci.pop(0))

    print(f'#{tc} {queue[0][0]})

    # pizza = []
    # index = 1
    #
    # #이 부분이 포인트 치즈의 인덱스 구하기 위해서
    # for cheese in Ci:
    #     pizza.append((cheese, index))
    #     index += 1
    # print(pizza)
    # pizza = []
    # for (idx, val) in enumerate(Ci, 1):
    #     pizza.append((idx, val))
    # print(pizza)




    print(pizza)
    print(f'#{tc} {Ci}')