numbers = ['포도', '토마토', '미나리']
N = 3

# numbers로 만들 수 있는 모든 경우의 수
# 1 << N == 2 ** N
# 1 왼쪽으로 3번 쉬프트 한다
# 0001 -> 1000
for x in range(1, 1 << N): # 100000
    # result = 0
    subset = []
    # 그 모든 경우의 수에서,
    # numbers의 y번째 요소가
    # x번 경우의 수에 사용되었는지를 판별
    # x번 경우의 수가 1일때 bit -> 0001
    # numbers의 y번째 요소(0번쨰 요소) -> (1 << y)
    # numbers의 0번째 요소가 0001 -> (1 << 0)
    # numbers의 1번째 요소가 0010 -> (1 << 1)
    for y in range(N):
        if x & (1 << y):
            # result += numbers[y]
            subset.append(numbers[y])
    # 부분집합의 요소가 2개 일때에만 출력
    # 미나리를 안쓴 경우만 출력
    if len(subset) == 2 and '미나리' not in subset:
        print(subset)
    # if result == 0:
    #     print(1)
    #     break