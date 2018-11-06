from rest_framework import serializers
from . import models


class ListStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stack
        fields = ('id', 'stack_data')


class RetrieveStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stack
        fields = '__all__'
