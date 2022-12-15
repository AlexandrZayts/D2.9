from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    Author_User = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.author_rating = Post.objects.filter(Post_Author=Author).values("post_rating") * 3 \
                             + Comment.objects.filter(Comment_User=Author).values("comment_rating") \
                             + Comment.objects.filter(Post_Author=Author).values("comment_rating")
        return self.author_rating


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category.title()


article = 'ar'
news = 'ns'
choic = [
    (article, 'статья'),
    (news, 'новость')
]


class Post(models.Model):
    Post_Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    position = models.CharField(max_length=2 ,choices=choic, default=news)
    post_time = models.DateTimeField(auto_now_add=True)
    Post_PostCategory = models.ManyToManyField(Category, through='PostCategory')
    post_header = models.CharField(max_length=64, default="Без темы")
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)


    def like(self):
        return self.post_rating + 1

    def dislike(self):
        return self.post_rating - 1

    def __str__(self):
        return f'{self.post_header.title()}: {self.post_text[:20]}' #!!!!2


class PostCategory(models.Model):
    PostCategory_Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    PostCategory_Category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    Comment_Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Comment_User = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(
        max_length=255)  # Из задания не ясно только авторизованные пользователи могут оставлять комментарии или нет, ограничения задано для исключения спама от гостей.
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        return self.comment_rating + 1

    def dislike(self):
        return self.comment_rating - 1

