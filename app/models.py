from django.db import models

# Create your models here.
class Post(models.Model):
    writer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    