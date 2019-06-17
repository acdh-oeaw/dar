# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class WebAppSerializer(serializers.HyperlinkedModelSerializer):
    app_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = WebApp
        fields = '__all__'
