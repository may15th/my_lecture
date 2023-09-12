import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box_num = [0] * (N)
    # print(N, Q)
    # print(box_num)

    # 1 슬라이싱 풀이
    # 이렇게 하면 슬라이싱한 후 언패킹한 값들을 i로 바꾸는 게 아니라
    # 슬라이싱 된 새로운 리스트 자체를 i로 바꾸려 하는거라 안되는 것!
    # 언패킹 한 후 값 넣는 법이 있나???
    for i in range(1, Q+1):
        li, ri = map(int, input().split())
        box_num[li-1:ri] = i
        print(box_num)

    #2 이중 for문 풀이 - 그냥 이중 for문으로 푼다고 생각,
    # 슬라이싱은 안되는 경우가 많다!!
    for i in range(1, Q+1):
        li, ri = map(int, input().split())
        for j in range(li-1, ri):
            box_num[j] = i


    # 언패킹 이용 출력
    print(f'#{tc}', end = ' ')
    print(*box_num)
