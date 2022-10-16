from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Mobile(models.Model):                #each class is going to be its own table in the DB
    brand=models.CharField(max_length=100)
    base_color=models.TextField()                  #text field will take unrestricted text
    model=models.TextField()
    battery_capacity = models.IntegerField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.brand