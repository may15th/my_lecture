N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

def conqure(n, lst):
    # 이중 리스트 안에 1이 없으면 조건 충족
    if not any(1 in i for i in lst):
        # 함수안에서 전역변수값을 가지고 쓸 때 전역변수 값을 변형
        lst_cnt.append(0)
        return
    # 이중 리스트안에 0이 없으면 조건 충족
    elif not any(0 in i for i in lst):
        lst_cnt.append(1)
        return
    else:
        lst_0 = []
        lst_1 = []
        for i in lst:
            lst_0.append(i[:n//2])
            lst_1.append(i[n//2:])
        conqure(n//2, lst_0[:n//2])
        conqure(n//2, lst_0[n//2:])
        conqure(n//2, lst_1[n//2:])
        conqure(n//2, lst_1[:n//2])
        return

lst_cnt = []
conqure(N, lst)
print(lst_cnt.count(0))
print(lst_cnt.count(1))


'''
input
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''
'''
output
9
7
'''