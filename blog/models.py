from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(default="picture.jpeg", upload_to="post_pictures")
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
# Create your models here.
