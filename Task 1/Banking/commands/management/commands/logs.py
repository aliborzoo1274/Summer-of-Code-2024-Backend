from django.core.management.base import BaseCommand
from django.db.models import Max, F
from account.models import Account
from person.models import Person
import os

class Command(BaseCommand):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', '..', '..', 'logs')

    def handle(self, *args, **kwargs):
        # self.list_of_owner_and_balance()
        # self.account_with_most_balance()
        # self.five_accounts_with_least_balance()
        # accounts_whose_id_is_greater_than_its_balance()
        self.accounts_where_the_national_id_of_the_account_holder_exceeds_its_balance()

    def list_of_owner_and_balance(self):
        query_set = Account.objects.all()
        account_list = list(query_set)

        final_file_path = os.path.join(self.file_path, 'list_of_owner_and_balance.txt')
        with open(final_file_path, 'w') as file:
            for i in account_list:
                file.write(f"Account_id: {i.id} | Owner_name: {i.person.first_name} {i.person.last_name} | Balance: {i.balance}\n")

    def account_with_most_balance(self):
        max_balance = Account.objects.all().aggregate(Max('balance'))['balance__max']

        final_file_path = os.path.join(self.file_path, 'account_with_most_balance.txt')
        with open(final_file_path, 'w') as file:
            file.write(str(max_balance))

    def five_accounts_with_least_balance(self):
        query_set = Account.objects.all().order_by('balance')[:5]

        final_file_path = os.path.join(self.file_path, 'five_accounts_with_least_balance.txt')
        with open(final_file_path, 'w') as file:
            for i in query_set:
                file.write(f"{i.balance}\n")

    def accounts_whose_id_is_greater_than_its_balance(self):
        query_set = Account.objects.filter(id__gt=F('balance'))

        final_file_path = os.path.join(self.file_path, 'accounts_whose_id_is_greater_than_its_balance.txt')
        with open(final_file_path, 'w') as file:
            if (len(query_set) == 0):
                file.write('Empty')
            for i in query_set:
                file.write(f"Account_id: {i.id} | Balance: {i.balance}\n")

    def accounts_where_the_national_id_of_the_account_holder_exceeds_its_balance(self):
        query_set = Account.objects.filter(person__national_id__gt=F('balance'))

        final_file_path = os.path.join(self.file_path, 'accounts_where_the_national_id_of_the_account_holder_exceeds_its_balance.txt')
        with open(final_file_path, 'w') as file:
            if (len(query_set) == 0):
                file.write('Empty')
            for i in query_set:
                file.write(f"Account_id: {i.id} | Owner_id: {i.person.national_id} | Balance: {i.balance}\n")