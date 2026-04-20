from django.db import models

from system.models import Farmer
from system.models import TimeStampMixin


class Transaction(TimeStampMixin):
    farmer = models.ForeignKey(Farmer, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DateTimeField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "transaction"

