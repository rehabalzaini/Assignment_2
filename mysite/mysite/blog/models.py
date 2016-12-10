from django.db import models

# Create your models here.
class entries(models.Model):

    name = models.CharField(max_length=220)
    description = models.CharField(max_length=530)