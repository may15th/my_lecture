from django.urls import path, include
from . import views

# appname 하나일떈 appname적을 필요 x

urlpatterns = [
    path('', views.index),
    path('example/', views.example),
]
