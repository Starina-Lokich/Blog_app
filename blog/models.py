from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) # Заголовок
    content = models.TextField() # Текст поста
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    author = models.CharField(max_length=100) # Автор поста

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Связь с постом
    text = models.TextField() # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания

    def __str__(self):
        return f"Комментарий к {self.post.title}"