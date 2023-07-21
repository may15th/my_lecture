list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전', 
    '원생몽유록', 
    '이생규장전', 
    '장화홍련전', 
    '수성지', 
    '백호집', 
    '홍길동전', 
    '만복자서포기'
    ]

# 모든 책이 있는 경우
# all_green = True
# 보유하지 않은책이 없는경우,
missing_book = False
for rental in rental_book:
    # 지금 문제 : 보유하지 않은 책을 발견한 순간 반복문 종료
    # 어떤 문제 : 보유하지 않은 모든 책을 출력하라.
    if rental not in list_of_book:
        # all_green = False
        missing_book = True
        print(f'{rental} 은 보유하고 있지 않습니다.')
        break
    # print(rental)
# 반복문 순회하면서, 한번도 조건문
# if rental not in list_of_book 을 통과한적이 없는경우,
# if all_green == True:
#     print('모든 책을 보유 하고 있습니다.')

if missing_book == False:
    print('모든 책을 보유 하고 있습니다.')