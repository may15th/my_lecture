from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail)
]
# mname template에서 쓰는데 template안쓰니깐...