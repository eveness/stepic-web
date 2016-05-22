from django.http import HttpResponse 

def first(request, *args, **kwargs):
    return HttpResponse('OK')