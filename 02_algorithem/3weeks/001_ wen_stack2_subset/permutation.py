# 순열
# 내가 가지고 있는 수로 만들 수 있는 모든 경우의 수
# 백트래킹 만드면서 후보군이란걸 만들었었다.

from itertools import permutations
arr = range(1,5)
perm = list(permutations(arr, 3))
print(perm)

comb = list(combinations(arr, 3))
print(comb)

# 나는 어느 상황에서 순열, 조합을 써야 할까?

