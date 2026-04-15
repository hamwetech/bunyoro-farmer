from django.urls import path, include

from system.views import ClanUploadView, GenderStatsView, FarmerMonthlyStatsView, FarmerWeeklyStatsView

urlpatterns = [
    path('dashboard/gender/', GenderStatsView.as_view(), name='gender-stats'),
    path('upload/clan/', ClanUploadView.as_view(), name='clan-upload'),
    path('farmers/monthly/', FarmerMonthlyStatsView.as_view(), name='bar-farmers-monthly'),
    path('farmers/weekly/', FarmerWeeklyStatsView.as_view(), name='bar-farmers-weekly'),
]