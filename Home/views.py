from django.shortcuts import render, HttpResponse
from Home.models import Post

# Create your views here.
def index(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")