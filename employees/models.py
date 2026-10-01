from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    leave_balance = models.IntegerField(default=20)

    def __str__(self):
        return self.name