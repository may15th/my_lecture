# # 순열

# # nPr : n개의 요소중, r개를 사용하여 순열

# # r : 내가 사용하고 있는 값의 수

# def perm(r):
#     # 재귀 함수
#     if r == N:
#         print(completed_perm)
#         return

#     else:
#         # 내가 가진 arr의 모든 원소를 매번 사용할 것인지 체크
#         for i in range(N):
#             # arr의 i번째 요소 쓴적이 있는지 없는지를 기준으로 판단
#             if not visited[i]: # i번째 쓰지 않았다면
#                 visited[i] = True
#                 completed_perm[r] = arr[i]
#                 perm(r+1) #재귀
#                 visited[i] = False


# arr = [1,2,3]
# N = len(arr)
# # 내가 perm 함수 호출 시 arr의 i번째 값을 썼었던 적이 있는지 판별 하기 위함.
# visited = [0] * N
# # 최종적으로 온성될 순열을 담아 둘 리스트
# completed_perm = [0] *N

# perm(0)


print('--순열--')


# 중복 순열

# nPr : n개의 요소중, r개를 사용하여 순열

# r : 내가 사용하고 있는 값의 수
# k : 사용할 실제 갯수

def perm(r, K):
    # 재귀 함수
    if r == K:
        print(completed_perm)
        return

    else:
        for i in range(N):
                completed_perm[r] = arr[i]
                perm(r+1,K) 



arr = [1,2,3]
N = len(arr)
completed_perm = [0] *N

perm(0,2)