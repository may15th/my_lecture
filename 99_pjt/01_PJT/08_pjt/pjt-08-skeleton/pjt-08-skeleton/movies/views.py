from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre

# Create your views here.
@require_safe
# get, head method만 받아들이는 데코레이터
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')

    comments = movie.comments.all()
    comment_form = CommentForm()
    
    context = {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movie/detail.html', context)

@require_safe
def recommended(request):
    pass


# recommende 까지만 만들고 팔로워, 같은 것들만 만들며 되는건가???