from django.core.management.base import BaseCommand
from account.models import Account

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        src = int(input("Who wants to transfer money? Please enter the account id: "))
        dst = int(input("Transfer money to who? Please enter the account id: "))
        value = int(input("How much money will be transfered? "))
        self.transfer_money(value, src, dst)
    
    def transfer_money(self, value, src, dst):
        src_account = Account.objects.get(id = src)
        src_account.balance -= value
        src_account.save()
        dst_account = Account.objects.get(id = dst)
        dst_account.balance += value
        dst_account.save()