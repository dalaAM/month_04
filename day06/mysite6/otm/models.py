from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return  self.name
class Book(models.Model):
    title = models.CharField(max_length=30,unique=True)
    name = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
