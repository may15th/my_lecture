import sys
sys.stdin = open('input.txt')

# 복도를 기준으로 번호를 정해보자

T = int(input())
for tc in range(1, T+1):
    N = int(input())      #학생 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    #복도를 나타내는 카운트 배열 필요
    cnt = [0] * 201 # 방 사이 공간을 지나는 사람 수
    for a, b in arr:    # a<=b 라는 보장이 없음.
        # min(a,b), max(a,b) 사용법 확인해두기
        # for i in range(a//2, (b+1)//2) 이렇게 하면 안된다고
        a = (a+a % 2)//2
        b = (b+b % 2)//2
        for i in range(min(a, b)//2, max(a, b)//2+1):
            cnt[i] += 1

    print(f'#{tc} {max(cnt)}')




