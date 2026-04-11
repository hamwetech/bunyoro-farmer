from django.urls import path
from .views import upload_locations

urlpatterns = [
    path("upload-locations/", upload_locations, name="upload_locations"),
]