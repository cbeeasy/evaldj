from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Frontpage1</h1>")