from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.CharField(max_length=20)
    uname=models.CharField(max_length=100)
    uemail=models.EmailField(max_length=100)
    ucontact=models.IntegerField()
