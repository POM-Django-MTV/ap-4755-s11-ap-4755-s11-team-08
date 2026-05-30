from django.http import HttpResponse

def order_page(request):
    return HttpResponse(
        "<h1>This is order app page! Congratulations!</h1>"
    )