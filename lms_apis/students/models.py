from django.db import models

from baseuser.models import baseUserModel

# Create your models here.


class Student(baseUserModel):
    program = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
    