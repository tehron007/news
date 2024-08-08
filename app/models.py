from django.db import models

class NewsModel(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    