from django.db import models

# Create your models here.

class Software(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
