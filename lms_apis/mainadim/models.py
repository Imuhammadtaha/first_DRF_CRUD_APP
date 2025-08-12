from django.db import models

from baseuser.models import baseUserModel

# Create your models here.
class MainAdmin(baseUserModel):
    
    def __str__(self):
        return self.name