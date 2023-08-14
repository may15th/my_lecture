def fibo(n):
    cur, next = 0, 1
    for _ in range(n):
        cur, next = next, cur + next
        print(cur)

fibo(3)
# 엄밀하게는 틀린 코드 n+1 이 출력됨

'''
fibo
0,1,1,2,3,5,8,13

8
'''