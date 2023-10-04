from django.urls import path
from . import views

app_name = 'accounts'
urlpattern = [
    # 1. django는 원칙적으로trailling slash를 작성하도록 권장.
    # /login/ 현재 경로에 login
    # login/ 루트 경로에 login
    path('login/', views.login, name='login'),

]