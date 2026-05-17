from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    eno =  models.IntegerField()
    ename =  models.CharField(max_length=30)
    esal = models.IntegerField()
    emobile = models.BigIntegerField()
    eadd =  models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
