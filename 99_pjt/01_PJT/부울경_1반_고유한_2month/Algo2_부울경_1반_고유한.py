import sys
sys.stdin = open('algo2_sample_in.txt')

#테스트케이스 입력
T = int(input())
for tc in range(1, T+1):
    # 카드 수, 김싸피 순서, A덱 입력
    N, M = map(int, input().split())
    Ai = list(map(str, input().split()))
    # 보너스 점수 0, b덱,c덱 빈 리스트로 초기화
    bonus = 0
    b = []
    c = []
    arr1 = []
    arr2 = []


    # print(N, M, Ai)

    # Ai의 숫자들 자료형을 str에서 int로 바꿔줌
    for i in range(N):
        if Ai[i] != '+':
            Ai[i] = int(Ai[i])
            if (Ai[i]+bonus) % 2 == 1:
                b.append(Ai[i] + bonus)
            if (Ai[i]+bonus) % 2 == 0:
                c.append(Ai[i] + bonus)

        elif Ai[i] == '+':
            bonus += 1

        # error뜨는 이유는 Ai[i]가 '+'인 경우 있기 때문
        # Ai[i]가 + 아닌 경우를 나타내는 if문 아래 있어야 한다. bonus는 어차피 아래쪽에서 for문 순회하면서 값 더해짐

        # if (Ai[i]+bonus) % 2 == 1:
        #     b_deck.append(Ai[i] + bonus)
        # if (Ai[i]+bonus) % 2 == 0:
        #     c_deck.append(Ai[i] + bonus)
    print(f'#{tc}')
    print(b)
    print(c)
    print('==============')


    for i in range(M):
        if c:
            arr1 = c.pop()

        if b:
            arr2 = b.pop(0)

        if i+


    print(f'#{tc}')
    print(arr1, arr2)