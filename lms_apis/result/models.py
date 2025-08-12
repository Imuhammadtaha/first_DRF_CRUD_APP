from django.db import models
from students.models import Student

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    marks = models.IntegerField()
    percentage = models.FloatField()
    declared_on = models.DateTimeField(auto_now_add=True)
    file_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.student.name} - {self.percentage}%   and {self.student.name} scored {self.marks}"
