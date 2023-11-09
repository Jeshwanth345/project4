from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def me(request):
    return HttpResponse('hi world...')
