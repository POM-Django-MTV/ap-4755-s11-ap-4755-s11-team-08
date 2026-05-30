"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Імпортуємо функції-представлення з кожного створеного додатка
from author.views import author_page
from book.views import book_page
from order.views import order_page
from user.views import user_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', author_page, name='author_page'),
    path('book/', book_page, name='book_page'),
    path('order/', order_page, name='order_page'),
    path('user/', user_page, name='user_page'),
]
