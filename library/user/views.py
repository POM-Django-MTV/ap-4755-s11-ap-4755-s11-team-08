from django.http import HttpResponse

def user_page(request):
    return HttpResponse(
        "<h1>This is user app page! Congratulations!</h1>"
    )