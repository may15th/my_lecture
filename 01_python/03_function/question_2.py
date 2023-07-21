def greeting(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요!')

# 모든 매개 변수에 키워드 인자 형식으로 값을 넘겼을 때.
greeting(age=30, name='홍길동')
print('첫', '두', '세', end='\t', sep=':')
print('다음 줄')

# 가변인자로 매개변수를 정의하면
# 함수를 호출 할 때, N개의 값을 넘겨도 모두 하나의 변수에 할당
# 이때, tuple 형태로 할당 된다.
def func(*args, sep=' '):
    print(args, sep)

func('첫', '두', '세')
