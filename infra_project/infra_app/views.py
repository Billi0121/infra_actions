from django.http import HttpResponse


def index(request):
    return HttpResponse("OOOO da")


def second_page(request):
    return HttpResponse("А это вторая страница WWW")
