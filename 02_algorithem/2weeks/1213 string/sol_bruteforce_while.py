'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.
위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
문장의 길이는 1000자를 넘어가지 않는다.
한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
한 문장에서는 하나의 문자열만 검색한다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.
[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input)
    p = input()
    t = input()
    # 패턴과 타겟 인덱스 조절 필요
    #1 while문 풀이
    # 조사대상 두개 패턴, 타겟의 인덱스 담을 변수 선언
    p_idx = 0
    t_idx = 0
    # 최종 결과값
    result = 0  # 패턴이 문장에 몇 번 들어가는지 셈.
    # 조사를 언제까지 반복?
    # 타겟 끝까지 조사하면서 패턴 몇 번 나오는지 세야한다.
    len_t = len(t)
    while t_idx < len_t:
        # 두 값이 같다면
        # if t[t_idx] == p[p_idx]:
        #     p_idx += 1
        #     t_idx += 1
        # else:
        #     if p_idx != 0:
        #         p_idx = 0
        #     p_idx = 0
            #타겟 인덱스는 그대로.

        #
        # t_idx번째 값과 p_idx번째 값이
        # 같거나 틀릴 때 취해야 하는 행동 정의
        if t[t_idx] != p[p_idx]:
            t_idx = t_idx - p_idx

            p_idx = -1

        # 같거나 틀린 상황 이외에
        # 모든 상황에 대해서
        #p_idx 와 t_idx는 증가 할 것
        p_idx += 1
        t_idx += 1

        if p_idx == len(p):
            result +=1 #패턴 한번 찾음.
            p_idx = 0 #다음 부터는 다스 0번부터 조사.
    print(f'#{tc}')

# 코드는 길게 보고 머리속으로 하나씩 다 세세하게 순서밟아가면서 생각해야함. 나처럼 단편적으로 보면 안된다.




    print(f'#{tc} {result}')