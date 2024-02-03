from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'text', 'rate')