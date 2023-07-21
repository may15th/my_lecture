number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
# 어려운 건 없다
# create_user 에 name, age, address 3 가지 매개 변수 넣고, user_info 딕셔너리도 정의

def create_user(name, age, address):
    increase_user()
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }
    print(f'{name}님 환영 합니다!')
    return user_info

print(create_user('홍길동', 30, '서울'))