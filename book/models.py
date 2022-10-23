from django.db import models

from user.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    price = models.FloatField(null=True, blank=True)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)