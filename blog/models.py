from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

LOCATION_CHOICES = [
    ('Mumbai', 'Mumbai'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('New Delhi', 'New Delhi')
]
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
GENRE_CHOICES = [
    ('Education', 'Education'),
    ('Tech', 'Tech'),
    ('Politics', 'Politics'),
]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(choices=LOCATION_CHOICES, max_length=50, blank=True)
    genre = ArrayField(
        models.CharField(max_length=50),
        size=3,
    )
    gender = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
