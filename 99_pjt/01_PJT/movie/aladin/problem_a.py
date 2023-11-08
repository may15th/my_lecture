import json
from pprint import pprint


def book_info(book):
    pass

    new_book={
        'id' : book.get('id'),
        'title' : book.get('title'),
        'author' : book.get('author'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover' : book.get('cover'),
        'categoryId' : book.get('categoryId')
    }

    return new_book

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))


### sample.json 파일을 data파일로 옮겨야 할 것 같다.
## 적절한 명령어가 있을 것 같은데 방법을 모르니까... sample.json을 복붙.

