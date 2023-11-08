from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from menus.models import Menu
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.register(User, UserAdmin)
admin.site.register(Menu)

#5 admin 사이트 메뉴 띄우기 위해서는 해당 모델 임포트 후 admin.site.register(모델명)입력.
