from rest_framework import viewsets, generics, pagination, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import django_filters
from .models import WebApp
from .serializers import WebAppSerializer
from .filters import WebAppListFilter
from django_filters.rest_framework import FilterSet


class WebAppViewSet(viewsets.ModelViewSet):
    queryset = WebApp.objects.all()
    serializer_class = WebAppSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = WebAppListFilter
    ordering_fields = '__all__'
