from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.db.models import Count, Q, Case, When, IntegerField
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from system.models import Farmer, Clan


def dashboard_callback(request, context):
    context.update({
        "custom_variable": "value",
    })

    return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # total_farmers = Farmer.objects.count()
        #
        # total_male = Farmer.objects.filter(gender='Male').count()
        # total_female = Farmer.objects.filter(gender='Female').count()
        # total_clans_with_farmers = Clan.objects.annotate(
        #     farmer_count=Count('farmer')
        # ).filter(farmer_count__gt=0).count()
        #
        # today = date.today()
        #
        # farmers = Farmer.objects.exclude(date_of_birth__isnull=True)
        #
        # youths = farmers.filter(
        #     date_of_birth__gt=date(today.year - 35, today.month, today.day)
        # ).count()
        #
        # adults = farmers.filter(
        #     date_of_birth__lte=date(today.year - 35, today.month, today.day)
        # ).count()
        #
        # youth_male = farmers.filter(
        #     gender='Male',
        #     date_of_birth__gt=date(today.year - 35, today.month, today.day)
        # ).count()
        #
        # youth_female = farmers.filter(
        #     gender='Female',
        #     date_of_birth__gt=date(today.year - 35, today.month, today.day)
        # ).count()
        #
        # adult_male = farmers.filter(
        #     gender='Male',
        #     date_of_birth__lte=date(today.year - 35, today.month, today.day)
        # ).count()
        #
        # adult_female = farmers.filter(
        #     gender='Female',
        #     date_of_birth__lte=date(today.year - 35, today.month, today.day)
        # ).count()
        #
        # farmers_per_clan = Farmer.objects.values('clan__name').annotate(
        #     total=Count('id')
        # ).order_by('-total')
        #
        # farmers_per_district = Farmer.objects.values('district__name').annotate(
        #     total=Count('id')
        # ).order_by('-total')
        #
        # farmers_per_clan_district = Farmer.objects.values(
        #     'district__name', 'clan__name'
        # ).annotate(
        #     total=Count('id')
        # ).order_by('district__name', '-total')

        today = date.today()
        farmers = Farmer.objects.all()

        youth_male = farmers.filter(
            gender='Male',
            date_of_birth__gt=date(today.year - 35, today.month, today.day)
        ).count()

        youth_female = farmers.filter(
            gender='Female',
            date_of_birth__gt=date(today.year - 35, today.month, today.day)
        ).count()

        adult_male = farmers.filter(
            gender='Male',
            date_of_birth__lte=date(today.year - 35, today.month, today.day)
        ).count()

        adult_female = farmers.filter(
            gender='Female',
            date_of_birth__lte=date(today.year - 35, today.month, today.day)
        ).count()

        data = {
            "total_farmers": farmers.count(),
            "total_male": farmers.filter(gender='Male').count(),
            "total_female": farmers.filter(gender='Female').count(),

            "total_clans_with_farmers": Clan.objects.annotate(
                farmer_count=Count('farmer')
            ).filter(farmer_count__gt=0).count(),

            "youths": farmers.filter(
                date_of_birth__gt=date(today.year - 35, today.month, today.day)
            ).count(),

            "adults": farmers.filter(
                date_of_birth__lte=date(today.year - 35, today.month, today.day)
            ).count(),

            "youth_male": youth_male,
            "youth_female": youth_female,
            "adult_male": adult_male,
            "adult_female": adult_female,

            "per_clan": list(
                farmers.values('clan__name').annotate(total=Count('id'))
            ),

            "per_district": list(
                farmers.values('district__name').annotate(total=Count('id'))
            ),

            "per_clan_district": list(
                farmers.values('district__name', 'clan__name')
                .annotate(total=Count('id'))
            )
        }
        context.update(data)

        return context


def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

class GenderStatsView(View):
    def get(self, request, *args, **kwargs):
        base = {'Male': 0, 'Female': 0}

        data = Farmer.objects.values('gender').annotate(total=Count('id'))

        for item in data:
            gender = item['gender']
            if gender in base:
                base[gender] = item['total']

        return JsonResponse({
            "labels": list(base.keys()),
            "data": list(base.values())
        })