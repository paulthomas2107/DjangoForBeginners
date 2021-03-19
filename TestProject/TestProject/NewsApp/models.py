from django.db import models
from django.utils import timezone

# Create your models here.


class Article3(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def ShortenText(self):
        return self.body[:100]


class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.place.name


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name


class Article2(models.Model):
    headline = models.CharField(max_length=300)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE),

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    headline = models.CharField(max_length=300)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.author


class SportsNews(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author


class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username
