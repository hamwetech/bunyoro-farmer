from django.db import models
from django.contrib.auth.models import User
from system.models import TimeStampMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        db_table = 'user_profile'


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print("SIGNAL FIRED")
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def refresh_auth_token(sender, instance=None, **kwargs):
    Token.objects.filter(user=instance).delete()
    Token.objects.create(user=instance)