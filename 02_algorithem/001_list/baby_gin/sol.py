T = int(input())
for tc in range(1,T+1):
    numbers = list(map(int,input().split()))

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[j] >numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]


                