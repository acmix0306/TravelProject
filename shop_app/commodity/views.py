from django.shortcuts import render

def commodity_view(request):
    return render(request, 'commodity/commodity.html')
