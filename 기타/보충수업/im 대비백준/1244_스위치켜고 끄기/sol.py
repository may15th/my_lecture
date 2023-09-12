import sys
sys.stdin = open('input.txt')

switch = int(input())
s_list = list(map(int, input().split()))
students = int(input())

# print(switch, s_list, students)   ## 디버깅용

def turn(j):
    if s_list[j] == 0:
        s_list[j] = 1
    elif s_list[j] == 1:
        s_list[j] = 0


for _ in range(students):
    gender, number = map(int, input().split())
    # print(gender, number)         ## 디버깅용
    print(gender, number)

    if gender == 1:
        # for문 number로 뛰우는 풀이
        for i in range(number, switch+1, number):
            turn(i-1)

        #2 while문 이용한 풀이
        # i =1 ##초기화 필요
        # while number * i <= number:
        #     turn(number*i-1)
        #     i += 1

    if gender == 2:
        turn(number-1)
        # 내 생각 풀이 아웃 오브 레인지 뜸
        # for i in range(switch):
        #     if s_list[number-1-i] == s_list[number-1+i]:
        #         turn(number-1-i)
        #         turn(number-1+i)

        # while문 이용 풀이
        i=1     #while을 for문 처럼 사용할 때는 i =1로 초기화 필요!!!!
        while 0<= number-1-i and number-1+i < switch and s_list[number-1-i] == s_list[number-1+i]:
            turn(number-1-i)
            turn(number-1+i)
            i += 1

    # elif gender == 0:
print(s_list)








