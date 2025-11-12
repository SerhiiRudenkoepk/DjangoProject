from django.db import models
from django.utils import timezone


# Create your models here.
# this is for data base.

# models are created through classes

class Category(models.Model):
    title = models.CharField(max_length=255) # this is a field for the category title
    created_at = models.DateTimeField(default=timezone.now)


# --- Course model ---
class Course(models.Model):
    title = models.CharField(max_length = 255) 
    price = models.FloatField() # float number 
    students_qty = models.IntengerField() # amount of students
    review_qty = models.IntengerField() # int for a score
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # when we will delete this category, everything will be deleted from this category