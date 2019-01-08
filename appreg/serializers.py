# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class WebAppSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WebApp
        fields = '__all__'
