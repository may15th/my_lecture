import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 갯수 부분 출력
    a_n = a.pop(0)
    b_n = b.pop(0)

    four_cnt = 0
    three_cnt = 0
    two_cnt = 0
    one_cnt = 0


    def count(arr):
        four_cnt = 0
        three_cnt = 0
        two_cnt = 0
        one_cnt = 0

        for i in arr:
            if i == 4:
                four_cnt += 1
            elif i == 3:
                three_cnt += 1
            elif i == 2:
                two_cnt += 1
            elif i == 1:
                one_cnt += 1

        ans = [four_cnt, three_cnt, two_cnt, one_cnt]
        return ans

    print(count(a))
    print(count(b))
    print('=========')
    for i in range(4):

        if count(a)[i] > count(b)[i]:
            print('A')
            break
        elif count(a)[i] < count(b)[i]:
            print('B')
            break
            
    # else를 이렇게 앞으로 뺄 수 있다 기억!!!!
    else:
        print('D')
