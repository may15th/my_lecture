# 딕셔너리 이용한 풀이
T = int(input())
word_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# 이것도 빈 리스트에 값 추가하는 형식 문제
a_dict = {}

# 총 10회 시행할 건데,
# a_dict[word_num[i]] word_numg의 요소들을 차례로 키값 넣고, 밸류 값을 0~9로 넣는다.
for i in range(len(word_num)):
    a_dict[word_num[i]] = i
# print(a_dict)     # 딕셔너리에 키, 밸류 들어갔는지 확인용


# order2는 #1,#2...#10까지 인풋 이고, N=길이
for order in range(1, T + 1):
    order2, N = input().split()
    N = int(N)
    array = list(input().split())


    new_array = []
    for i in range(N):
        new_array.append(a_dict.get(array[i]))

    new_array

