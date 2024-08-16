from django.core.management.base import BaseCommand
from person.models import Person
from account.models import Account
from django.db import connection

class Command(BaseCommand):
    help = 'Delete all instances and reset primary key sequence for MyModel'

    def handle(self, *args, **kwargs):
        # Delete all instances
        Person.objects.all().delete()
        Account.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all instances of MyModel.'))

        # Reset primary key sequence
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='person_person';")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='account_account';")
        self.stdout.write(self.style.SUCCESS('Reset primary key sequence for MyModel.'))