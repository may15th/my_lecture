def fibo1(n):
    global memo
    if n < 2:
        return n
    elif n >=2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n=7
memo = [0] * (n+1)


print(fibo1(n))

'''
fibo
0,1,1,2,3,5,8,13
0,1,2,3,4,5,6,7
'''