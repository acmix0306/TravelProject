from django.db import models

# Create your models here.

#Types.CommodityInfos 定義商品資訊及類別
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    firsts = models.CharField('商品第一分類', max_length=100)
    seconds = models.CharField('商品第二分類', max_length=100)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = '商品類型'
        verbose_name_plural = '商品類型'


class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('商品名稱', max_length=100)
    seizes = models.CharField('顏色規格', max_length=100)
    types = models.CharField('商品類型', max_length=100)
    price = models.FloatField('商品價格')
    discount = models.FloatField('折扣後價格')
    stock = models.IntegerField('庫存數量')
    sold = models.IntegerField('售出數量')
    likes = models.IntegerField('收藏數量')
    created = models.DateField('上架日期', auto_now_add=True)
    img = models.FileField('商品主圖', upload_to=r'imgs')
    details = models.FileField('商品介紹', upload_to='details')

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = '商品資訊'
        verbose_name_plural = '商品資訊'


