from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
        Custom user model manager where email is the unique identifier
        for authentication instead of usernames.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email= email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    """
        Inheriting AbstractBaseUser class to create custom user class
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.email
    
    @property
    def full_name(self):
        return self.first_name + self.last_name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    
class Country(models.Model):
    """
        Country model with all given fields
    """
    continent_choices = {
        ('Asia', 'asia'),
        ('Europe', 'europe'),
        ('North America', 'north america'),
        ('Africa', 'africa'),
        ('Oceania', 'oceania'),
        ('Antarctica', 'antarctica'),
        ('South America', 'south america'),

        
    }
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=52, null=False)
    continent = models.CharField(max_length=20, choices=continent_choices, null=False, default='Asia')
    Region = models.CharField(max_length=26, null=False, default='')
    surfacearea = models.FloatField(null=False, default='0.00')
    indepyear = models.IntegerField(null=True)
    population = models.IntegerField(null=False, default='0')
    lifeexpectancy = models.FloatField(null=True)
    GNP = models.FloatField(null=True)
    GNPOld = models.FloatField(null=True)
    localname = models.CharField(max_length=45, null=False, default='')
    governmentform = models.CharField(max_length=45, null=False, default='')
    headofstate = models.CharField(max_length=60, default=None, null=True)
    capital = models.IntegerField(default=None, null=True)
    code2 = models.CharField(max_length=2, null=False, default='')


    def __str__(self) -> str:
        return self.name
    

class city(models.Model):
    """
        city model with all given fields
    """
    name = models.CharField(max_length=35, null=False, default='')
    countrycode = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    district = models.CharField(max_length=20, null=False, default='')
    population = models.IntegerField(null=False, default=0)

    def __str__(self) -> str:
        return self.name

class countrylanguage(models.Model):
    """
        country language model with all given fields
    """
    countrycode = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    language = models.CharField(max_length=30, null=False, default='')
    isofficial = models.BooleanField(null=False, default='F')
    percentage = models.FloatField(null=False, default='0.0')

    def __str__(self) -> str:
        return self.language
