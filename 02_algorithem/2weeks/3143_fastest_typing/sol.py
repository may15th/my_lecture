import sys
sys.stdin = open('input.txt')

#테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):
    #target, pattern 입력
    A, B = map(str, input().split())
    # bruteforce_while문 사용
    A_idx = 0
    B_idx = 0
    result = 0
    len_A = len(A)
    while A_idx < len_A:
        if A[A_idx] != B[B_idx]:
            A_idx = A_idx - B_idx
            B_idx = -1

    B_idx += 1
    A_idx += 1

    if B_idx == len(B):
        result += 1
        B_idx = 0
    print(f'#{tc} {result}')




# A안에 B가 몇개 들어있는지 찾고 나머지 + 들어있는 개수 = 누르는 횟수
# brute force / while
T = int(input())
for tc in range(1, T+1):
    A, B = input().split() # 전체 문자열, pattern
    len_a = len(A)
    len_b = len(B)
    idx_a = 0
    idx_b = 0
    cnt = 0
    # print(len_a, len_b) # test
    while idx_a < len_a:
        # 다를때 > 한칸 이동하고 처음부터
        # print(idx_a, idx_b)
        if A[idx_a] != B[idx_b]:
            idx_a = idx_a - idx_b
            idx_b = -1
        # 무조건 둘 다 증가
        idx_a += 1
        idx_b += 1
        if idx_b == len_b:
            cnt += 1
            idx_b = 0 # 얘도 다시 처음부터 비교해야하니까
    ans = len_a - (len_b*cnt) + cnt

    print(f'#{tc} {ans}')