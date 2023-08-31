# 규칙성 못찾을 경우 정렬 후 규칙성 찾기!
# 컨테이너 무게와 딱 맞는 트럭으로 옮기는 게 좋을 것 가지만
# 어차피 최대무게 트럭이 최대무게 컨테이너를 옮기지 않을 경우 그보다 작은 컨테이너를 옮길 것이기 때문에
# 의미가 없다.   greedy로 풀면 되나?
# 컨테이너 무게, 운반 가능 무게 트럭도 내림차순으로 정렬
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    # [1] 내림차순 정렬
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)

    # [2] 짐을 하나씩 내리면서 트럭에 적재 가능한지 체크
    ans = i = 0
    for n in lst1:
        if n <= lst2[i]:    # 짐을 나를 수 있는 경우
            ans += n
            i += 1
            if i == M:  #트럭이 없는 경우
                break



    print(f'#{tc} {ans}')

# greedy 하게 푸는 경우 대부분 풀이 복잡하지 않아
# n이 복잡하고 갯수 많을 수록 가능한 모든 겨웅 조합하기 보다는 그리디한 규칙으로 푸는 경우 많아
# 이렇게 해서 될까 찜찜할 수 있지만
# 많은 경우 정렬을 동반해 규칙성을 찾는 풀이 쓴다는 것 기억!!!!!!

