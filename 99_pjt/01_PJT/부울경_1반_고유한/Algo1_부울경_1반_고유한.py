'''
3
3
123
4
2
0A
A
3
8F5
A

'''
# 테스트 케이스 입력
T =  int(input())
# 16진수의 자릿수 갯수, 16진수(이후 for문 돌리기위해 리스트 입력), P와 XOR 연산할 16진수 key값 입력.
for tc in range(1, T+1):
    N = int(input())
    P = list(input())
    key = input()

    #'#tc'출력 부분
    print(f'#{tc}', end = ' ')
    #
    for i in range(N):
        # XOR연산하기 위해 P의 각 자릿수와,key값 A~F 를 10~15로 바꿔줌
        if P[i] == 'A':
            P[i] = int(10)

        elif P[i] == 'B':
            P[i] = int(11)

        elif P[i] == 'C':
            P[i] = int(12)

        elif P[i] == 'D':
            P[i] = int(13)

        elif P[i] == 'E':
            P[i] = int(14)

        elif P[i] == 'F':
            P[i] = int(15)


        if key == 'A':
            key = int(10)

        elif key == 'B':
            key = int(11)

        elif key == 'C':
            key = int(12)

        elif key == 'D':
            key = int(13)

        elif key == 'E':
            key = int(14)

        elif key == 'F':
            key = int(15)

        ans = int(P[i]) ^ int(key)

        # ans값은 10진수로 표현되기 때문에 ans값 10~15를 A~F로 바꿔줌
        if ans == 10:
            ans = 'A'

        elif ans == 11:
            ans = 'B'

        elif ans == 12:
            ans = 'C'

        elif ans == 13:
            ans = 'D'

        elif ans == 14:
            ans = 'E'

        elif ans == 15:
            ans = 'F'

        # 나온 값들을 붙여서 출력
        print(ans, end ='')
    #띄어쓰기로 다음 테스트케이스와 구분
    print()