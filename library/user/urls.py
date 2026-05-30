from django.urls import path
from .views import user_page

urlpatterns = [
    path('', user_page),
]