from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    image = models.ImageField()
    brith_date = models.DateField()

    def __str__(self):
        return self.first_name


class Positions(models.Model):
    title = models.CharField(max_length=220)
    employees = models.OneToOneField(Employees, on_delete=models.CASCADE)
