from django.db import models

# Create your models here.
class Student(models.Model):
	Gender = (('M','Male'),('F','Female'))
	name = models.CharField(max_length = 256)
	roll_no = models.IntegerField()
	gender = models.CharField(max_length = 1,choices = Gender)
