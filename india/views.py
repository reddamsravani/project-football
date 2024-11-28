from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def india(request):
    return HttpResponse('<h1><marquee>SUNIL CHHETRI IS CAPTAIN OF INDIA</marquee></h1>')
