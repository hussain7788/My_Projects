from django.db import models
from django.utils import timezone

# Create your models here.


class TodoModel(models.Model):
    t_name = models.TextField(max_length=100)
    t_cr_date = models.DateTimeField(timezone.now)
    t_due_date = models.DateTimeField(blank=True)
    t_completed = models.IntegerField(default=0)


    def __str__(self):
        return self.t_name