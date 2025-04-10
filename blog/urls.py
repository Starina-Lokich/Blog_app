from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, post_list, post_detail, add_comment

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Маршруты API под префиксом 'api/'
    path('', post_list, name='post_list'),  # Главная страница (список постов)
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Страница поста
    path('post/<int:pk>/add_comment/', add_comment, name='add_comment'),  # Добавление комментария
]