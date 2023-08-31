# idx :이번 회차 조사 시작 지점
def comb(now, r, idx):
    if now ==r:
        print(check)
        print(check[:r])    #r개까지만 보여줘 이런 풀이도 가능함!!
    else:
        for i in range(idx, len(num)):
            check[now] = num[i]
            comb(now+1, r, i+1)   #중복 없는 조합
            # comb(now+1, r, i)   #중복 있는 조합




# 재귀면 stack이다.


num = [1,2,3]
#실제 조합에 구성되는 요소들을 담을 리스트
check = [0] * len(num)
comb(0,2,0)


## 요리사 문제 풀어보기 swea

### 베이비진 greedy한 풀이

