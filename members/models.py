from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email= models.CharField(max_length=255 , default="")
    phone= models.CharField(max_length=255 , default="")
    address=models.TextField(default="Syria")
    
    def __str__(self):
        return f'{ self.pk} {self.firstname} {self.lastname}'
