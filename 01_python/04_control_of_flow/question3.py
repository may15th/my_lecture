# 조건문을 작성하고 있는 와중인데...

for i in range(3):
    if i == 1:
        # 어떤 엄청 복잡한 작업
        pass
    else:
        print(i)

numbers = [1, 2, 3]
print(enumerate(numbers))
print(list(enumerate(numbers)))

a, b = (1, 2)
# print(a, b)

# [(0, 1), (1, 2), (2, 3)]
#   ( 0,    1)
for index, item in enumerate(numbers):
    print(index, item)