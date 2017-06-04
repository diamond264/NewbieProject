from django.db import models


# Create your models here.

class Category(models.Model):
    area = models.CharField(max_length=30)
    korName = models.CharField(max_length=30)

    def __str__(self):
        return self.area


class Board(models.Model):
    name = models.CharField(max_length=30)
    korName = models.CharField(max_length=30)
    categoryId = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    boardId = models.ForeignKey(Board)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
