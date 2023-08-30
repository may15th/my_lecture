import sys
sys.stdin = open('input.txt')

# row: 현재 조사 대상
# chosen: 선택 대상
# 완전검색을 할거다.
    # 모든 N개의 원소를 다 조사 했는지 판단

# run triplet 찾을 것. 둘 다 있으면 베이비 진
# 0번째 있는 값을 어디에 사용했는지 기록

#순열로 풀이, chosen에 인덱스 번호 새겨줌.
def perm(row, chosen):
    if row == N:
        for i in chosen:
            print(data[i], end = ' ')
        print()
        return

    # 모든 N개의 원소를 조사 했는지 판단
    for i in range(N):
        # i번째 에 쓰겠다고 이전에 판정된 적이 있다면,
        # 현재 조사 대상을 i번째에 쓸 수 없으므로.
        if i in chosen:
            continue
        chosen[row] = i # row번째 대상을 i번째에 둬서 사용하겠다.
        perm(row+1, chosen)
        chosen[row] = -1

for tc in range(1):
    N = 6
    data = input()
    # i번째에 들어 갈 수 있는 수 0, N-1을 제외한
    chosen = [-1] * N
    perm(0, chosen)