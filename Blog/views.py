from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def blog(request):
    return HttpResponse("This is kathan sheth here")
