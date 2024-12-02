from django.shortcuts import render

def shopper_view(request):
    return render(request, 'shopper/shopper.html')
