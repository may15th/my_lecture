def f(i, N, s):     # s : i-1원소까지 부분집합의 합(포함된 원소의 합)
    global
    if i == N:
        if s == 10:
            print(bit)
        return
    else:
        bit[i] = 1
        f(i+1, N, s + A[i])
        bit[i] = 0
        print(bit, end = ' ')
        ㅔ갸ㅜge(N):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        print(f': {s}')
        return
    else:
        bit[i] = 1              # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        return

A = [1,2,3]