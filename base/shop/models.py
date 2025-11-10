from django.db import models
from django.utils import timezone


# Create your models here.
# this is for data base.

# models are created through classes

class Category(models.Model):
    title = models.CharField(max_length=255) # this is a field for the category title
    created_at = models.DateTimeField(default=timezone.now)