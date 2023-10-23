from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
    # 사용자가 경로에 작성한 정수
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article>/likes/', views.likes, name='likes')
]
