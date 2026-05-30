from django.urls import path
from .views import order_page

urlpatterns = [
    path('', order_page),
]