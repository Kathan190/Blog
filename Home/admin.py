from django.contrib import admin
from Home.models import Blog2
from Home.models import Blog1
from Home.models import Contact
from Home.models import SimpleBlog1
# Register your models here.

admin.site.register(Blog1)
admin.site.register(Blog2)
admin.site.register(Contact)
admin.site.register(SimpleBlog1)
