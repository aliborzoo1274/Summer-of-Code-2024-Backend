from django.core.management.base import BaseCommand
from django.db.models import Max
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
        return

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