from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="posts/")
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.username