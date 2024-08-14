from django.db import models
from person.models import Person

class Account(models.Model):
    balance = models.PositiveIntegerField()
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)