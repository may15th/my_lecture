# 1. 카운팅 배열을 사용하는 방법
import sys
sys.stdin = open('input.txt')


def baby(cnts, idx):
    if cnts[idx] == 3:
        return 1
    for i in (idx-2, idx-1, idx):       # range로 안 두고 이렇게 값들 튜플로 둘 수도 있다.
        if 0<=i<=7 and cnts[i] > 0 and cnts[i+1] >0 and cnts[i+2] >0:
            return 1
    return 0





T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    # [1] cnts1, 2 배열 생성(빈도수 체크)
    cnts1 = [0] * 10
    cnts2 = [0] * 10

    ans = 0
    for i in range(len(lst)):
        if i % 2 == 0:  # 짝수 => 1번 플레이어
            cnts1[lst[i]] += 1
            if baby(cnts1, lst[i]):
                ans = 1
                break

        else:
            cnts2[lst[i]] +=1
            if baby(cnts2, lst[i]):
                ans = 2
                break

    print(f'#{tc} {ans}')



