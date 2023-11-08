import json
from pprint import pprint


def books_info(books, categories):
    # 여기에 코드를 작성합니다.  
    pass
    
    categoryNamelist = []
    category_id_list = books.get('categoryId')
    for category in categories:
            if category.get('id') in category_id_list:
                categoryNamelist.append(category.get('name'))
                
    new_book={
        'id' : books.get('id'),
        'title' : books.get('title'),
        'author' : books.get('author'),
        'priceSales' : books.get('priceSales'),
        'description' : books.get('description'),
        'cover' : books.get('cover'),
        'categoryName' : categoryNamelist
    }

    return new_book   



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))