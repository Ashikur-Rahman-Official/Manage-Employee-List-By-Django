from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.mobile_number)