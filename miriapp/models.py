from django.db import models
from django.urls import reverse

class Company(models.Model):
    name=models.CharField(max_length=250)
    logo=models.FileField()
    website=models.CharField(max_length=250)
    email=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name+" - " +self.email

class Employee(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=255)

    def get_absolute_url(self):

        return reverse('detail', kwargs={'pk': self.company.id})

    def __str__(self):
        return self.first_name+" - " +self.last_name
