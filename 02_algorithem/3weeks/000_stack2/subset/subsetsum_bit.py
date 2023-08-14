# arr = list(range(1,11)) #1~10
# n = len(arr)    #길이가 10인 모든 경우의 수

# 2 ** n
# 1 << n

for i in range(1 << n):
    # 모든 경우의 수에 대해서 
    # 만들 수 있는 부분집합
    subset = []
    for j in range(n):
        #i 번째 경우의 수일때,
        #j번째 요소를 쓰니 마니?
        if i & (i << j):
            subset.append(arr[j])
    print(subset)
   
    # 부분집합의 합이 10이냐
    if sum(subset) == 10:
        print(subset)
