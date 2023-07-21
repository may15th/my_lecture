# book 파일에서 decrease_book 함수를 호출 한다.
from book import decrease_book
# ws_3_3.py
# 호출한 decrease_book 함수를 rental_book함수 아래 그냥 넣는다
def rental_book(name, number):
    decrease_book(number)

    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)
