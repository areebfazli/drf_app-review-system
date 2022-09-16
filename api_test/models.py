from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    qualification = models.CharField(max_length=500)
    gender = models.CharField(max_length=10)
    acceptance = models.BooleanField(null=True)
