from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def japan(request):
    return HttpResponse('<h1><marquee>WATARU ENDO IS CAPTAIN JAPAN</marquee></h1>')
