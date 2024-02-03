from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Review

class ReviewSerializer(Serializer):
    name = serializers.CharField(max_length=32)
    text = serializers.CharField()
    rate = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def create(self, validated_data):
        return Review.objects.create(**validated_data)