from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.TextField() 
    desc = models.TextField()
    summary = models.TextField(default="its okay")