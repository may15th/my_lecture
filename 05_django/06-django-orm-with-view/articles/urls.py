from django.urls import path
from . import views

app_name = 'articles'   #articles라는 태그를 다는 것.
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # 아래부터 create
    path('new/', views.new, name='new'),
    path('create/', view.create, name='create')
    # 템플릿을 주는 게 아님. 사용자 입력 데이터를 받아서 데이터베이스에 저장하는 view함수.
]
# 해당되는 위 url을 사용하게 될 때 articles.index 이런식으로 url 태그를 작성하게 됨.
