from rest_framework import viewsets
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# view-функция для отображения списка постов
def post_list(request):
    query = request.GET.get('q')  # Получаем поисковый запрос из параметров
    posts = Post.objects.all().order_by('-created_at')

    if query:  # Если есть поисковый запрос
        posts = posts.filter(Q(title__icontains=query))  # Ищем посты по заголовку

    paginator = Paginator(posts, 5)  # Разбиваем посты на страницы (по 5 на страницу)
    page_number = request.GET.get('page')  # Получаем номер текущей страницы
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'query': query})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Получаем пост по ID
    return render(request, 'blog/post_detail.html', {'post': post})

def add_comment(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        text = request.POST.get('text')  # Получаем текст комментария из формы
        if text:
            comment = Comment.objects.create(post=post, text=text)  # Создаем новый комментарий
            # Возвращаем JSON-ответ с данными нового комментария
            return JsonResponse({
                'id': comment.id,
                'text': comment.text,
                'created_at': comment.created_at.strftime('%d.%m.%Y %H:%M')
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)