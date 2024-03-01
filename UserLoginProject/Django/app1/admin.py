from django.contrib import admin
from .models import Customer
# Register your models here.
# admin.site.register(UserModel)


@admin.register(Customer)
class UserList(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 
                    'email', 'dob', 'phone']
