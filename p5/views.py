from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>welcome to the project</marquee>")
def home(request):    
    return render(request,"first.html")
def second(request):
    return render(request,"directory/second.html") 
def third(request):
    return render(request,"directory/third.html",context={'data':"mallika",'name':"sweety"})