from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
#2. 
from django.conf import settings
# conf = configure 설정이라는 뜻.
# -> 문자열 -> model.py에 작성할 떄는 문자열로 적는 게 좋다


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        # Meta 안에 있는 필드들만 필드로 받겠다. 그럼 회원가입창이 간결해짐.
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
