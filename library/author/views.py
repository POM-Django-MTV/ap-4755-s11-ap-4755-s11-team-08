from django.shortcuts import render

def author_page(request):
    return render(request, 'author/index.html')

