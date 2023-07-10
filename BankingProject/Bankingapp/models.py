from django.db import models

# Create your models here.
class Login(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    desc=models.TextField()


    def __str__(self):
        return self.name




