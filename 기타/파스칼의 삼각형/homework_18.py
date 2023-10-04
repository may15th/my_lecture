T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # arr 빈 리스트 만든 후에
    arr = []

    # arr2를 0 1개 0 2개 0 3개 ... 이를 하나씩 빈 리스트에 넣어줘서 이중 리스트만들기.
    for i in range(N):
        arr2 = [0 for _ in range(i+1)]
        arr.append(arr2)

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1

            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        print(*(arr[i]))