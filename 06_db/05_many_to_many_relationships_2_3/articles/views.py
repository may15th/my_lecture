from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def main(request):
    # BASE_DIR/articles/templates/articles/main.html

    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/main.html', context)

def create(request):
    # 게시글 생성을 위한 form이 필요하네...?
    if request.method == 'POST':
        form = ArticleForm()
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('main')
    else:
        formf = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    
    article = Article.objects.get(pk=article_pk)
    context = {
        ''
    }
    
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        
    else:
        article.like_users.add(request.user)