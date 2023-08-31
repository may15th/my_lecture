# now : 현재 조사 위치
# r : 최대 조사 대상 수
# 눈여겨 봐야 하는 건 
# 1. 저장 2. 조건 3. 반복이 다임 남의 코드 봤을 때 변수를 눈여겨 볼 것.

def perm(now, r):
    if now ==r:
        print(check)
        return
    else:
        # 완전 검색
        for i in range(len(num)): 
            if not visited[i]: continue
            visited[i] = True   # i번째 요소를 쓴다?
            # 실제 사용 여부는 check에 표기
            check[now] = num[i]
            perm(now + 1,r) #조사위치를 다음 칸으로 옮겨준다.


import itertools

# 반복에 대한 이해
# 완전 검색: brute force에 대한 이해
# 재귀 함수에 대한 이해 
# 3가지 목적으로 순열을 학습함.

num = [1,2,3]

# 각 요소의 사용여부
visited = [0] * len(num)

# 왜 만들어야 하나.
# visited 안쓰고 원본 없앨 수도 있지만 반복할 것. 반복해서 똑같은 행위 실행할텐데
# 원본 바꾸는 것은 순회의 범위를 바꿔버릴 수 있어.
visited = [0] * (len(num) + 1)

# 실제 순열에 구성되는 요소들을 담을 리스트
check = [0] * len(num)

perm(0,2)






