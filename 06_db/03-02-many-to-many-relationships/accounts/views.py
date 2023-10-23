from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    #user의 디테일 페이지
    #user를 조회
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
        
    }
    return render(request, 'accounts/profile.html', context)

#좋아요 코드와 99%유사
def follow(request, user_pk):
    User = get_user_model() #의미를 모르겠다
    you = User.objects.get(pk=user_pk)
    me = request.user
    
    # 내가 상대방의 팔로워 목록에 있다면
    if me in you.followers.all():
        # 팔로우 취소
        you.followers.remove(me)
        # me.follwings.remove(you)
    else:
        you.followers.add(me)
        # me.followings.add(you)
    return redirect('acoounts:profile', you.username)
    
    
    # follow하는 대상을 조회
    
    # follow 취소/진행에 대한 기준
    
    # follow 버튼 토글
    pass


# 오류 99%는 오타니깐 오류 뜬 부분 한 번 읽어보고, 자기가 낸 오타 잘 못찾는 법이니 gpt문의하자...!
