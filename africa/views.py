from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def africa(request):
    return HttpResponse('<h1><marquee>VIRAT KOHLI IS CAPTAIN AFRICA</marquee></h1>')

