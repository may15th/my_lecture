'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''

# 코드 오류 뜨는데, 다시 확인./.;..

# 1. 재귀 돌리면서 숫자를 붙인다.
# 2. 숫자가 7자리가 되면
# 3. set에다 넣는다.

#설계 메모장에 적은 것 주석 그대로 옮기고, 그냥 적기만 하면돼.


# 특정 위치를 기점으로 상하좌우 문자를 붙여야 하므로
# 파라미터로 좌표값도 받아야 한다.

def dfs(y, x, number):
    # 길이가 7이되면 재귀 종료
    if len(number) == 7:
        # 추가적인 작업
        result.add(number)
        return

    for k in range(4):
        nj = j +dj[k]
        ni = i +di[k]

        # 갈 수 없는 ㅟ치면 continue
        if nj <0 or nj>=4:
            continue

        if ni < 0 or ni >=4:
            continue

        # 갈 수 있다면, 다음 위치로 ㄱㄱ
        dfs(nj,ni, number+maps[nj][ni])



T = int(input())
dj = [-1,1,0,0]
di = [0,0,]

for tc in range(1, T+1):
    # 서로다른 수를 합친다 => 문자열이 더 좋다
    maps = [input().split() for _ in range(4)]

    # 7자리 수를 중복 제거하여 저장
    result = set()

    # 시작 지점을 모두 보아야 한다.
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')
