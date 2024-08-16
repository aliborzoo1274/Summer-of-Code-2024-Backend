from django.core.management.base import BaseCommand
from account.models import Account
from person.models import Person
import random
from faker import Faker # Should be installed

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_persons() # First we will create 5000 random persons.
        self.create_accounts() # In the second step we will create 20000 random accounts.

    def create_persons(self):
        fake = Faker()
        instances = []
        for _ in range(5000):
            name = fake.name()
            first_name = name.split()[0]
            last_name = name.split()[1]
            national_id = random.randint(1111111111, 9999999999)
            instances.append(Person(first_name = first_name, last_name = last_name, national_id = national_id))

        Person.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Creating random people completed.'))
    
    def create_accounts(self):
        instances = []
        for _ in range(20000):
            balance = random.randint(0, 20000000000)
            person = Person.objects.get(id=random.randint(1, 5000))
            instances.append(Account(balance = balance, person = person))

        Account.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Creating random accounts completed.'))