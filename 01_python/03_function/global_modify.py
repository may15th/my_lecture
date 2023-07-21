global_var = '글로별 값'
age = 3
def update_value(global_var): # 매개 변수 -> local scope
    print(global_var, '매개 변수로 받은 값')
    result = global_var * 3 # 글로벌 변수가 가지고 있던 값 활용 가능
    global_var = '로컬 값' # 글로벌 변수에 할당된 값에 영향 없이 다른값 재할당 가능
    return result
# 애초에 안되게 하지 왜 되게해서 헷갈리게 하나요?
# 1. 막아 놨습니다.
# 2. 코드 내가 씁니다. 규칙에만 맞춰서 잘 쓰면 편하게 쓸 수 있다.

print(update_value(global_var)) # 인자로 global scope 변수를 넘김
print(global_var)

