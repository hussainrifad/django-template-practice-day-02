from django.http import HttpResponse

def homePage(request):
    return HttpResponse('go to 8000/menu')