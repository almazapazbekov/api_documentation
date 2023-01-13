from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Position(models.Model):
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.position


class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    birthdate = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.fullname}, {self.user}'
