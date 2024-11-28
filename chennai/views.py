from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chennai(request):
    return HttpResponse('<h1><marquee>RUTURAJ IS CAPTAIN CHENNAI</marquee></h1>')
