from django.db import models

# Create your models here.

class Staff(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.FloatField()
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name
    