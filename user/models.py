from django.db import models
from django.contrib.auth.models import User
from system.models import TimeStampMixin


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        db_table = 'user_profile'
