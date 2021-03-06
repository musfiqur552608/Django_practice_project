import imp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

# Create your views here.
def error_404_view(request, exception):
    return render(request, '404.html')

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

def images(request):
    return render(request, 'image.html')

def image(request, imgname):
    image = str(imgname)
    image = image.lower()
    if image == "django":
        var = True
    elif image == "python":
        var = False
    dict = {
        "var" : var
    }
    return render(request, 'image.html', context=dict)

def intro(request, name, age):
    mydict = {
        "name" : name,
        "age" : age,
    }
    return JsonResponse(mydict)


def myform(request):
    return render(request, 'myform.html')


def submitform(request):
    dict = {
        "var1" : request.POST['mymail'],
        "var2" : request.POST['mypass'],
        "method" : request.method
    }
    return JsonResponse(dict)


def dform(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            dict = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
            if errorflag != True:
                dict["success"] = True
                dict["successmsg"] = "Form Submitted"
            
            dict["error"] = errorflag
            dict["errors"] = Errors

            return render(request, 'dform.html', context=dict)
    
    elif request.method == "GET":
        form = FeedbackForm()
        dict = {
            "form" : form
        }
        return render(request, 'dform.html', context=dict)




