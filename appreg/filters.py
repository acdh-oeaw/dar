import django_filters

from dal import autocomplete
from django import forms
from django.contrib.auth.models import User

from . models import WebApp


class WebAppListFilter(django_filters.FilterSet):

    class Meta:
        model = WebApp
        fields = "__all__"
