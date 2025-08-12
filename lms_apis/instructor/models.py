from django.db import models

from baseuser.models import baseUserModel


# Create your models here.
class Instructor(baseUserModel):
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.name
    
    