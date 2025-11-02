from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=8)
    joined_on = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.position}"