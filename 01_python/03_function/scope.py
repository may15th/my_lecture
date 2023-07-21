age = 100

def parent_func():
    age = 30

    # local scope
    def child_func():
        # global 변수 age의 값을 내가 바꾸고 싶다.
        global age
        age = 20
        print(age, 'child_func')
    
    child_func()
    print(age, 'parent_func')

parent_func()
print(age, 'global')
# print(numbers)