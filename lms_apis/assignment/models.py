from django.db import models
from instructor.models import Instructor
# Create your models here.

class Assignment(models.Model):
    
    announcement = models.CharField(max_length=100)
    
    file_url = models.URLField(max_length=500)
    

    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="assignments")



    published_on = models.DateTimeField(auto_now_add=True )
    
    deadline = models.DateTimeField()
    
    
    def __str__(self):
        
        return f"{self.announcement} by {self.instructor}"