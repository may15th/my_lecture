'''
10
5 16
3 1 3 5 6
2 10
7 7
3 120
83 64 36
4 416
299 239 116 128
5 1535
351 228 300 623 954
10 2780
268 61 201 535 464 168 491 275 578 153
10 1162
73 857 502 826 923 653 168 396 353 874
15 8855
3711 576 9081 3280 1413 6818 5142 2981 1266 484 5757 2451 6961 4862 2086
15 57209
8903 5737 3749 8960 724 6295 1240 4325 8023 3640 2223 639 4161 5330 4260
20 78988
3811 2307 3935 5052 4936 3473 6432 7032 1560 1992 5332 7000 4020 9344 2732 8815 9924 8998 9540 4640
'''

# 파라미터를 뭐 줘야할까?
# 전체를 다 뽑는 경우 점원의 길이만큼 주는 것.
# 문제 풀려면 점원 높이 점점 쌓으면서 재귀함수 돌려야 해.

# 재귀함수 4단계 기억
def recur(level, acc_height):

    global ans

    # 가지 치기
    # 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요가 없다!

    if acc_height >= B:
        ans = min(ans, acc_height)
        return


    if level == N:
        return

    # 해당 점원을 탑에 쓸 경우
    recur(level +1, acc_height +arr[level])

    # 안 쓸 경우
    recur(level +1, acc_height)



    # 들어 가기 전 (가지치기) [1,2,3,4] 에서 2를 선택했다면 1을 다시 볼 이유가있는가?
    # 1,2든 2,1이든 똑같이 3 이런 형식은 트리형식으로 생각하면 굉장히 좋아.


    # 다음 재귀 함수 호출


    # 돌아왔을 때




T= int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9) # 대충 엄청 큰 숫자
    recur(0,0)
    print(f'#{tc} {ans-B}')