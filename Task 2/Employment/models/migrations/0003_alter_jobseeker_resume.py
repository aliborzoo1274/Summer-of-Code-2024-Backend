# Generated by Django 5.0.8 on 2024-08-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes/'),
        ),
    ]