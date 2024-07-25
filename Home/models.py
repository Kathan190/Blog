from django.db import models

# Create your models here.

class Blog1(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    
class Blog2(models.Model):
    sno = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.email