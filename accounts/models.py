from django.db import models

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=250,)
    password=models.CharField(max_length=250)





