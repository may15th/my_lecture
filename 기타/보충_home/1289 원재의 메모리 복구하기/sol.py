# 다 읽을 필요 없어. 입력과 출력부터 읽어라.
# 이후 이해 안되는 부분 짚어 읽으면 돼.
import sys
sys.stdin = open('input.txt')


# 설계
# 테스트 케이스를 입력받는다
T= int(input())
print('t', T)
# 테스트 케이스만큼 반복한다
for tc in range(1, T+1):
# 테스트 케이스 순번을 표시한다
    print(tc)
# 메모리의 원래 값을 받는다
    memory = input() #그냥 받아주세요
    print('memory', memory)
# 수정한 횟수를 카운트할 변수를 준비한다 (count = 0)
    cnt = 0
    print('cnt', cnt)
    # 직전 값과 일치하는지 비교할 이전 값 변수를 준비한다 (prev = 0)
    prev = '0'  #문자열 0으로 넣어주면 최초 비교 이슈x    #애초에 0이니까 0으로 준비한다 => 최초에 기본값이 0인데 1로 바꿀 떄 문제가 생기므로...
    print('prev', prev)
# - 애초에 0이니까 0으로 준비한다
# 메모리의 원래 값을 순서대로 탐색한다
    for m in memory: # range 풀이도 추가적으로 해볼게요
        print(m, end = ' ') # m -> 가로로 볼게
        # todo : 현재 메모리값과 직전값을 비교한다
        # 다르다면 -> 일괄로 해서 바꿔줄 것이기 때문에 비트 수 변화가 이 경우에만 일어나게 됨
        if m != prev: # m-> 이번에 검사하려는 비트와 prev -> 직전에 저장한 비트값이 다를 경우에
            print(prev, m, type)  # 타입 차이 발생
            # 뒤에 있는 걸 일괄 m으로 바꿔야 하지만... 어차피 원래 메모리를 검사하니깐....
            cnt += 1 # 값을 늘려줌.
            prev = m # 직전 저장값을 md으로 바꿔줌
            print('*', end = ' ')
        # prev = m # 이렇게 둬도 됨. 근데 계산낭비임.

        # todo : 다르다면 count+=1 하고 prev를 해당 값으로 고쳐줌
    print() # 줄 바꿈

    # 수정한 횟수를 출력한다
    print('cnt', cnt)

# 현재 메모리값과 직전값을 비교한다
# 다르다면 count+=1 하고 prev를 해당 값으로 고쳐줌

# 수정한 횟수를 출력한다

# 세 가지 문제
# 1. 어떤 문법 함수를 끌어와야할 지 모른다
# 2. 구조화를 못한다 - > 손코딩
# 3. 디버깅, 출력을 안(못)한다

# 디버그 출력문을 다해 봐야 한다

# 정답 본 다음에 그냥 출력해버리고 제출해버리고 끝?
# 아니에요.


######### # 풀이 2 range 이용 풀이
for i in range(1, len(memory)+1):
    if i!= 0:
        prev = memory[i-1]
    else:
        prev = '0'

    if memory[i] != memory[i-1]:
    m= memory[i]

    if m != prev