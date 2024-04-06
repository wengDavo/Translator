from django.db import models

# Create your models here.
class Language(models.Model):
    title = models.TextField()
    code = models.TextField()

def __str__(self):
    return self.title