from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
def Raj(request):
    return HttpResponse('<h1> Raj have no money</h1>')


def peachu(request):
    return HttpResponse('peachu is foodie')