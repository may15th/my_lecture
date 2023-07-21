dusts = [60, 50, 66, 70]

# dust = dusts[0]
# print(dust)
# dust = dusts[1]
# print(dust)
# dust = dusts[2]
# print(dust)
# dust = dusts[3]
# print(dust)

# for item in dusts:
#     print(item)

# list -> sequence type 데이터 : 순서가 있다.
# list -> 길이를 알 수 있다. len(list)
# range -> 0 ~ n-1 까지의 숫자 범위를 만들 수 있다.
# range -> sequence type, iterable
# for 특성 | iterable 한 값이 가지고 있는 각 요소들을, 
#           임시 변수에 할당해서 코드를 실행
# for문으로 range를 순회 하면, range가 가지고 있는 0부터 n-1 까지의 값을 순회

# print(list(range(3)))

dusts = [60, 50, 66, 70]
# print(len(dusts)) # 4
# print(range(len(dusts))) # range(0, 4) -> 0, 1, 2, 3

for index in range(len(dusts)):
    dusts[index] = 0
    # print(dusts[index])
print(dusts)

# print('='*30)
# for dust in dusts:
#     print(dust)