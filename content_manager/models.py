from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Register(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname


