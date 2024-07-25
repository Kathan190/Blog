from django.shortcuts import render, HttpResponse
from Home.models import Blog1
from Home.models import Blog2
# Create your views here.
def index(request):
    allBlog1 = Blog1.objects