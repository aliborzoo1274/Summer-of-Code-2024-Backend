from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Job(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='job_photos/')
    validity_date = models.DateField()
    category = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    working_hours = models.CharField(max_length=255)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user.username