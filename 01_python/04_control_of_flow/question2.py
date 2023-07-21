numbers = [
#    0  1  2    
    [1, 2, 3], # 0

#    0  1  2
    [4, 5, 6], # 1

#    0  1  2
    [7, 8, 9]  # 2
]

for numbers_index in range(len(numbers)): 
    # print(numbers_index)
    scores = numbers[numbers_index]
    for scores_index in range(len(scores)):
        print(numbers[scores_index][numbers_index])

