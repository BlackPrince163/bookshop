from django.db import models


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
    description = models.CharField(max_length=500)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    price = models.FloatField(null=True, blank=True)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title