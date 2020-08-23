from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=20)
    pub = models.CharField('出版社', max_length=20)
    price = models.DecimalField('价格', max_digits=6, decimal_places=2)
   