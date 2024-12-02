from django.urls import path
from . import views

app_name = 'shopper'

urlpatterns = [
    path('', views.shopper_view, name='shopper'),
]