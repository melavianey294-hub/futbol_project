from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Hola! Esta es la vista de inicio.")
