from django.shortcuts import render


# Create your views here.

# 主頁
def shop_mainPage(request):
    return render(request, 'shop_app/shop.html')

#Register
def register(request):
    return render(request, 'shop_app/login.html')
