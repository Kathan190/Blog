from django.shortcuts import render, HttpResponse
from Home.models import Blog1
from Home.models import Blog2
# Create your views here.
def index(request):
    allBlog1 = Blog1.objects.all()
    allBlog2 = Blog2.objects.all()
    context = {'allBlog1':allBlog1, 'allBlog2':allBlog2}
    return render(request, 'index.html', context)
    #return HttpResponse('This is blog page')
