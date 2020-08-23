from django.db import models

# Create your models here.

class BookStore(models.Model):
    title =models.CharField("书名",max_length=50)#字段
    price =models.DecimalField('定价',max_digits=5,decimal_places=2)#涉及到金额的都用decimal这个数据类型
    #后添加的字段一定要执行确认值（2）,或者在新增字段内添加默认值,否则会造成迁移错误
    market_price =models.DecimalField('市场价',max_digits=5,decimal_places=2,default=0.0)
    publish =models.CharField('出版社',max_length=50,default='')
