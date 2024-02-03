from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .forms import ReviewCreateForm
from .filters import ReviewFilter
from .serializers import ReviewSerializer


class ReviewsList(ListView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'ReviewsApp/review_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        res = super().get_context_data(object_list=None, **kwargs)
        res['form']=self.filterset.form
        return res
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ReviewFilter(self.request.GET,queryset=queryset)
        return self.filterset.qs

class ReviewCreate(CreateView):
    form_class = ReviewCreateForm
    template_name = 'ReviewsApp/review_form.html'
    def form_valid(self, form):
        form.instance.user_from = self.request.user
        return super().form_valid(form)

class ReviewGetAPIView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        return Response(ReviewSerializer(reviews, many=True).data)

class ReviewPostAPIView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)