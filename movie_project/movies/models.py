from django.db import models
from categories.models import Category
from users.models import CustomUser
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', null=True)
    description = models.TextField(null=True)
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=255, null=True)
    writer = models.CharField(max_length=255, null=True)
    musician = models.CharField(max_length=255, null=True)
    cast = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField(null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
