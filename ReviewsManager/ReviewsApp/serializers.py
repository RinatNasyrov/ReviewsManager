from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Review
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'text', 'rate']
    def create(self, validated_data):
        return Review.objects.create(**validated_data)