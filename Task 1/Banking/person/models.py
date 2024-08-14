from django.db import models
from django.core.validators import MaxValueValidator

class Person(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    national_id = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999999)]
    )