number_of_people = 0


def increase_user():
    # global number_of_people
    number_of_people += 1
    #global number_of_people 안 칠경우 global nuimber_of_people 에 +1이 불가함. local 변수가 할당되지 않았다고 뜸.

# def increase_user(number_of_people):
#     number_of_people += 1
#     return number_of_people


increase_user()
# number_of_people = increase_user()
print(number_of_people)
