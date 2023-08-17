# 리스트 전체요소 나누기 2하려면 아래처럼 해야됨...

a= [2,2,2]
a = [a[i]//2 for i in range(len(a))]
print(a)