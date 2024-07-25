from django.shortcuts import render
from Home.models import Blog1
from Home.models import Blog2
from Home.models import Contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    allBlog1 = Blog1.objects.all()
    allBlog2 = Blog2.objects.all()
    context = {'allBlog1':allBlog1, 'allBlog2':allBlog2}
    return render(request, 'index.html', context)
    #return HttpResponse('This is blog page')
