# 테스트 갯수 입력
T = int(input())
# 테스트 갯수 만큼 테스트케이스 순회
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 최종 결과값
    result = 0
    for i in range(1, N+1):
        for j in range(0, N, i):
            result += arr[j]

    if result < 0:
        result = 0

    print(result)