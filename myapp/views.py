from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    sad = "I am said."
    happy = "Please make me happy"
    list = ["Give me freedom", "All is well", "I love this", "I am happy"]
    age = 23
    check = age > 18

    mydict = {
        "sad" : sad,
        "happy" : happy,
        "list" : list,
        "check" : check,
        "age" : age,
    }
    return render(request, 'second.html', context = mydict)

def image(request):
    return render(request, 'image.html')

def intro(request, name, age):
    mydict = {
        "name" : name,
        "age" : age,
    }
    return JsonResponse(mydict)



