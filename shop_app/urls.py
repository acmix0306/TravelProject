from django.urls import path
from . import views
from .views import register # 導入 register 視圖

urlpatterns = [
    path('', views.shop_mainPage, name='shop'),
    path('register/', views.register, name='register'), # 使用 register 函數
]

