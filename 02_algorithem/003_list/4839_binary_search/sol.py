def binary_search(ppage, end)









T = int(input())
for tc in range(1,T+1):
    P, A, B = map(int,input().split()) #P=책의 전체 쪽 수, A =
    t_a = binary_search(P,A)
    t_b = binary_searcg(P, B)
    if t_a ==t_b:
        print(f'#{tc} 0')
    elif t_a > t_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} A')