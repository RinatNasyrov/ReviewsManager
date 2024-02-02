from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Review
class ReviewsList(ListView):
    model = Review
    queryset = Review.objects.all()