from django.db import models
from instructor.models import Instructor

class Lecture(models.Model):
    lecture_url = models.URLField(max_length=500)
    subject_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='lectures')
    
    published_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.subject_name} by {self.instructor.name}"