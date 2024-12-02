from django.urls import path, include # 確保 include 導入
from . import views # 定義 views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop_app/', include('shop_app.urls')), # 使用 include ,並確保包含shop_app 的 url
]
