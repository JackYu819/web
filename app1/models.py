from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __init____(self):
        pass

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __init__(self):
        pass
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __init__(self):
        pass

    def __str__(self):
        return self.name


class Entry(models.Model):
    def __init__(self):
        super(Blog, self).__init__()

    # blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

