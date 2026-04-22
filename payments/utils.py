import datetime
from django.db import transaction as db_transaction
from payments.models import Transaction


def create_transaction(farmer, amount, tx_type, category):

    with db_transaction.atomic():

        last_balance = farmer.account_balance

        if tx_type == 'CREDIT':
            new_balance = last_balance + amount
        else:
            new_balance = last_balance - amount

        transaction = Transaction.objects.create(
            farmer=farmer,
            amount=amount,
            transaction_type=tx_type,
            category=category,
            balance=new_balance,
            transaction_date=datetime.date.today(),
        )
        farmer.account_balance = new_balance
        farmer.save()
        return transaction