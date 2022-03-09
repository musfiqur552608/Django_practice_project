from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'second.html')

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydict = {
        "name" : name,
        "age" : age,
    }
    return JsonResponse(mydict)



