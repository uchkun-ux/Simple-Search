from django.db import models

# Create your models here.
class Employees(models.Model):
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Employees'

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    job = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name