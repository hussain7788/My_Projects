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

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)

# class UserModel(AbstractBaseUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=50, unique=True, null=False)
#     dob = models.DateField(null=True, blank=True)
#     phone = models.CharField(max_length=15, null=True, blank=True)

#     objects = CustomUserManager()
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     def __str__(self) -> str:
#         return self.username
    
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
    
