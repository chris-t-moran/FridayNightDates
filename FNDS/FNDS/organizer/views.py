from django.http import HttpResponse


def greeting(request):
    return HttpResponse('Hello World! This is the organizer page')

# Create your views here.
