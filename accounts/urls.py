from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('check', views.check, name='check'),
    path('payment', views.payment, name='payment'),
    path('sent', views.sent, name='sent'),
    path('success', views.success, name='success'),


]