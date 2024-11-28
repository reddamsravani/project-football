from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def germany(request):
    return HttpResponse('<h1><marquee>JOSHUA KIMMICH IS CAPTAIN OF GERMANY</marquee></h1>')

