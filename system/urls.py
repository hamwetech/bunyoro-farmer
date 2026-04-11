from django.urls import path, include

from system.views import GenderStatsView
from system.views import ClanUploadView

urlpatterns = [
    path('dashboard/gender/', GenderStatsView.as_view(), name='gender-stats'),
    path('upload/clan/', ClanUploadView.as_view(), name='clan-upload'),
]