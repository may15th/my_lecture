from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<author_name>', views.detail, name='detail'),
]
