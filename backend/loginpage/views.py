from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'login-page.html')
    # return HttpResponse("this is the login page")

def home(request):
    return HttpResponse("this is the home page")

def symptoms(request):
    return HttpResponse("this is the symptom checker page")

def checkarea(request):
    return HttpResponse("this is the to check area")

def safeport(request):
    return HttpResponse("this is the page for safeport")