def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))

'''
fibo
0,1,1,2,3,5,8,13
0,1,2,3,4,5,6,7
'''