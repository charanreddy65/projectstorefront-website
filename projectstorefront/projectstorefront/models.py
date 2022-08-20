import email
from django.db import models
from datetime import datetime



class Online_Shoping(models.Model):
    tittle=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    product= models.CharField(max_length=100)
    created_by = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.tittle

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name