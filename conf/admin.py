from django.contrib import admin
from django.apps import apps
from .base_admin import BaseAdmin


app_models = apps.get_app_config("conf").get_models()

for model in app_models:
    try:
        admin.site.register(model, BaseAdmin)
    except admin.sites.AlreadyRegistered:
        pass
