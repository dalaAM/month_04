from django.db import models




# Create your models here.
class User(models.Model):
    username=models.CharField('用户名',max_length=20)
    age=models.IntegerField('年龄',default='0')
    def __str__(self):
        return '%s - %s'%(self.username,self.age)

