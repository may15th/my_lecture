# 회의실 배정 cpu task 배정 등 굉장히 다양하게 활용되는 문제

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    print(f'#{tc} {ans}')



# 짧은 작업시간만 하면 되나?
# 반례찾으면 안되는 것.
# 먼저 시작한 작업을 먼저 배정?
# 이것도 아님.

#*** 먼저 끝나는 작업을 하면 된다!!!! 작업 갯수 기준일 떼***###
## 이런 문제 유형은 회의실 배정 작업 등 엄청나게 많이 사용 한다!

# [1] 종료시간 기준(오름차순 정렬)


