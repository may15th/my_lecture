#카운팅 정렬로 풀어야 되는 건 알겠다.
#counting정렬 확인 해서 풀기

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = input()
    cnt_list = []
    for i in range(N):
        cnt = 1
        for j in range(N):
            if i == j:
                continue
            if arr[i] == arr[j]:
                cnt += 1
        cnt_list.append(cnt)




    print(f'#{tc} {result}')
