from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=90)
    roll=models.IntegerField()
    marks=models.IntegerField()
    avg=models.FloatField()

    def __str__(self):
        return self.name