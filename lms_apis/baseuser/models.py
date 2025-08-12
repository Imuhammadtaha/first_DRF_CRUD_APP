from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class baseUserModel(models.Model):
    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20)  
    pic_url = models.URLField(max_length=500)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name