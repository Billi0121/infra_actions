from django.http import HttpResponse


def index(request):
    return HttpResponse("О да маквин готов")


def second_page(request):
    return HttpResponse("А это вторая страница WWW")

#dddD