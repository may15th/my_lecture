import json
from pprint import pprint


def book_info(book, categories):
    pass
    # 여기에 코드를 작성합니다.  

    categoryNamelist = []
    category_id_list = book.get('categoryId')
    
    for category in categories:
        if category.get('id') in category_id_list:
            categoryNamelist.append(category.get('name'))
            
    new_book={
        'id' : book.get('id'),
        'title' : book.get('title'),
        'author' : book.get('author'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover' : book.get('cover'),
        'categoryName' : categoryNamelist
    }
                

    return new_book



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))

print(book_info)



# def book_info(book,categories):

#     # 장르명이 담길 리스트 생성
#     categoryNameList = []

#     # 전달받은 책의 카테고리 id 리스트
#     category_id_list = book.get('categoryId')

#     # 카테고리 id/이름이 담긴 리스트를 반복하면서
#     for category in categories:
#         # 카테고리 id가 책의 카테고리 리스트에 포함된 카테고리 명을 List에 추가
#         if category.get('id') in category_id_list:
#             categoryNameList.append(category.get('name'))

#     # 완성된 장르명 리스트 바탕으로 새로 딕셔너리 데이터 만들기
#     new_data = {
#         'id':book.get('id'),
#         'title':book.get('title'),
#         'author':book.get('author'),
#         'priceSales':book.get('priceSales'),
#         'description':book.get('description'),
#         'cover':book.get('cover'),
#         'categoryName': categoryNameList
#     }
#     return new_data