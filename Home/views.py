from django.shortcuts import render
from Home.models import Blog2
from Home.models import Blog1 
from Home.models import Contact
from Home.models import SimpleBlog1
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    allBlog2 = Blog2.objects.all()
    simpleblog1 = SimpleBlog1.objects.all()
    context = {'allBlog2':allBlog2, 'simpleBlog1':simpleblog1}
    return render(request, 'index.html', context)
    #return HttpResponse('This is blog page')

def about(request):
    return render(request, 'about.html')

def blogpost(request, id):
    post = Blog1.objects.filter(post_id = id)[0]
    return render(request, 'blogpost.html', {'post':post})