def some_func(parm1):
    return parm1 ** 2

print(some_func(3))
print(some_func)

other_var = some_func
print(other_var(3))

numbers = [3]
print(list(map(other_var, numbers)))

# map 함수를 쓸 때 변수가 하나면 오브젝트가 그대로 반환되고, 변수가 여러개면 언패킹이 되는건가요?? 

def my_map(func, iterable):
    for item in iterable:
        result = func(item)
        print(result, end=' ')

my_map(some_func, numbers)
'''
map 쓸때
numbers = [1, 2, 3]
result = map(str, numbers)
result1, result2 = map(str, numbers)

이런 경우가 궁금해서여!
'''
print()
print('=====')
numbers = [1, 2]
result = list(map(str, numbers))
print(result)

result1, result2 = map(str, numbers)

print(result1, result2)