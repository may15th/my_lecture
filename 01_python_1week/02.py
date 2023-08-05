# # # 진법 변경 왜 안되지??
# # 똑같이 썼는데 이제 또 된다...?
# print(bin(12))
# print(oct(12))
# print(hex(12))

# print(2/3)

# print(5/3)

# a = 3.2-3.1 #0.10000000000
# b = 1.2-1.1 #0.09999999987

# #1. 임의의 작은 수 활용
# #아래식은 무슨 뜻이지?
# print(abs(a-b) <= 1e-10) # True

# #2. math 모듈 활용
# import math
# print(math.isclose(a,b)) #True

# math module의 isclose함수 활용

# f-string
bugs = 'roaches'
counts = 13
area = 'livingroom'

print(f'Debugging {bugs}{counts}{area}')

greeting = 'hi'
print(f'{greeting:^10}')
print(f'{3.141592:.4f}')
# 내림이 아니라 반올림 해서
# 3.1415가 아니라 3.1416이 됨

# 1. 슬라이싱 잘 모르겠다.
#인덱스 접근 가능 순서 있는 자료형
#슬라이싱이란...?
#    0 1   2   3   4
#      | | | | |
list = [1, 2, 3, 4, 5]
# print(list[100])
# #indexerror뜸
print(list[1:100])
#슬라이싱 쓸때는 범위 벗어나도 오류 없이 잘 나오니 주의할 것.
#list[start :end: step]
#start에 작성한 내용은 그 index번호 부터 시작.
#end에 작성한 내용은 그 index-1번째 까지 출력
#step에 작성한 내용은, start부터 end까지 step 만큼 건너뛰면서

print(list[1:100])

print()
print(None)
# ```프로그래밍 언어 학습시 가장 헷갈려 하는 것.
# 값이 있음 ''빈문자열 빈문자열이라는 값이 있음
# False  값이 없음을 나타내는 값이 있는 것.
# [] {} None은 사용자 아이디 0 값을 아무것도 안넣어 공백 조차 안넣어. 
