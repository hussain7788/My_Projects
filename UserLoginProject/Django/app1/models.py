from django.db import models
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False)
    dob = models.DateField(null=False)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
