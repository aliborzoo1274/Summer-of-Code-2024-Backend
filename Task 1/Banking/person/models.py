from django.db import models

class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    national_id = models.PositiveIntegerField(max_length=10)