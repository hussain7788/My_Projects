from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Address(models.Model):
    """
    Address
    """
    customer = models.ForeignKey(User, verbose_name=_(
        "Customer"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone = models.CharField(_("Phone Number"), max_length=50)
    Email = models.EmailField(_("Email"), max_length=50)

    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(
        _("Address Line 2"), max_length=255, default="", null=True)
    postcode = models.CharField(_("Postcode"), max_length=50)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return "Address"
