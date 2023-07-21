# 5번만 반복 되도록 하고싶다.
dust = [1, 2]
result = 0
while result < 5:
    # print('점심시간')
    # print('점심시간 끝')
    # print(result)
    result += 1
    for i in range(2):
        print(dust[i], 'for')
        break
    print()
    print(result, 'while')
    print('==')