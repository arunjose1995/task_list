from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
