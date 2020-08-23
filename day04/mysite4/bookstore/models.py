from django.db import models


# Create your models here.
#模型类新建一张表
class book(models.Model):
    #'verbose_name' 主要在前端显示书名，'max_length'表示字符长度，'unique=True' 表示唯一
    title =models.CharField(verbose_name='书名',max_length=50,unique=True)
    #'decimal_places'表示小数点后几位
    price =models.DecimalField(verbose_name='定价',max_digits=5,decimal_places =2)
    market_price =models.DecimalField(verbose_name='零售价',max_digits=5,decimal_places =2)
    pub =models.CharField(verbose_name='出版社',max_length=50)
    # 'default'表示默认值  数据库中的内容不能随意删除，可以给一个标记，如果标记为不活跃用户，表示用户已经被删除
    is_active =models.BooleanField(verbose_name='是否活跃',default=True)

    def __str__(self):
        return  '%s - %s - %s - %s'%(self.title,self.price,self.market_price,self.pub)

class Author(models.Model):
    #'verbose_name' 主要在前端显示书名，'max_length'表示字符长度，'unique=True' 表示唯一
    name =models.CharField(verbose_name='姓名',max_length=10,null=False)
    #'decimal_places'表示小数点后几位
    age =models.IntegerField(verbose_name='年龄',null=False)
    email =models.EmailField(verbose_name='邮箱',null=True)

    def __str__(self):
        return '%s -%s -%s'%(self.name,self.age,self.email)


class diver(models.Model):
    diver_name = models.CharField('司机名称',max_length=10)
    commany_name = models.CharField('公司名称',max_length=10,null=True)
