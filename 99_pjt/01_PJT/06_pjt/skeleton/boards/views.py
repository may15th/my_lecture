from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.

## article 부분 
@require_http_methods(["GET"])
def index(request):
    boards = Board.objects.all().order_by('-created_at')
    context = {
        'boards': boards
    }
    return render(request, 'boards/index.html', context)

@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')

    comments = board.comments.all()
    comment_form = CommentForm()
    
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.user == board.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
    else:
        return redirect('boards:index')
    
    context = {
        'board': board,
        'form': form,
    }        
    return render(request, 'boards/update.html', context)


# board.user = 현재 로그인된 유저 넣어준 다음에 저장
# commit값에 저장 db에 요청보내지는 않고 저장
# 이후 board.user에 대한 값 넣고, request.user값을 넣는다.

# form.save() form인스턴스 쓰는 이유.
# board는 model 의 인스턴스 form은 modelform의 save modelform은 save되는 순간 생성과 삭제를 구분 가능.

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)

@login_required
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.user == board.user:
        board.delete()
    return redirect('boards:index')

## comments 부분

@require_http_methods(["POST"])
def comment_create(request, board_pk): #댓글 작성하는 comment_create 코드임.
    board = get_object_or_404(Board, pk=board_pk)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.board = board
            comment.user = request.user
            comment_form.save()
            return redirect('boards:detail', board.pk)
    context = {
        'board':board,
        'comment_form':comment_form
    }        
    return render(request, 'boards/detail.thml', context)

#이전 create부분
# def comments_create(request, pk):
#     board = Board.objects.get(pk=pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.board = board
#         comment.user = request.user
#         comment_form.save()
#         return redirect('boards:detail', board.pk)
#     context = {
#         'board':board,
#         'comment_form':comment_form,
#     }
#     return render(request, 'boards/detail.html', context)

        

@require_http_methods(["POST"])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('boards:detail', article_pk)
        