from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name