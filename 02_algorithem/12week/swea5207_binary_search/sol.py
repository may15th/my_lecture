import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # 조사 방향
    def binarysearch(low, high, target, D):

        global result

        #중간값
        mid = (L+R)//2


        # 중간 값의 위치가 == 대상이라면
        if A[mid] == K:

            # 좌우, 반복하면서 찾아낸 대상! 횟수 1증가
            result += 1
            return

        # 타겟이 중간값보다 크면?
        elif A[mid] <T:
            #이전번에 오른쪽에서 왔으면 종료!!!! 아 이렇게 하면 되는 구나 ㅋㅋㅋㅋㅋ
            if D == 'RIGHT':
                return
            # 오른쪽으로 조사 보낼 것.
            binarysearch(mid+1,R,K,'RIGHT')
        # 타겟이 중간값보다 작으면?
        else:
            # 이전번에 왼쪽에서 왔으면 종료!!!
            if D == 'LEFT':
                return

            # 왼쪽으로 조사 보낼 것.
            binarysearch(L,mid-1,K,'LEFT')



    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    cnt_left, cnt_right = 0, 0

    # print(N,M)
    # print(A)
    # print(B)


    # B 전수조사
    for idx in range(M):
        if binarysearch(0, N-1, B[idx]) >= 0:
            cnt += 1
        # print(i)
        # print(cnt)
        # print(A)

    print(f'#{tc} {cnt} {cnt_left} {cnt_right}')

    # print(f'#{tc} {ans}')

    # 번갈아 가면서 탐색했는지를 알아야 해해