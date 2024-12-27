from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def hey(request):
#     return render (request, "entue/index.html")

def fm(request):
    return render (request, "entue/form.html")

def eduard(request):
    return HttpResponse("Hello , Eduard!")

def salute(request, name):
    return render(request, "entue/salute.html", {"name": name.capitalize()})