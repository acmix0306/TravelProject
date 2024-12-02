from django.db import models

# Create your models here.
STATE = (
    ('等待付款', '等待付款'),
    ('已付款', '已付款'),
    ('出貨中', '出貨中'),
    ('已簽收', '已簽收'),
    ('退貨中', '退貨中'),
)

class CartInfos(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField('購買數量')
    commodityInfos_id = models.IntegerField('商品ID')
    user_id = models.IntegerField('用戶ID')

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = '購物車'
        verbose_name_plural = '購物車'


class OrderInfos(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField('訂購總價')
    created = models.DateField('建立時間', auto_now_add=True)
    user_id = models.IntegerField('用戶ID')
    state = models.CharField('訂單狀態', max_length=20, choices=STATE)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = '訂單資訊'
        verbose_name_plural = '訂單資訊'