from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Review
from .forms import ReviewCreateForm


class ReviewsList(ListView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'ReviewsApp/review_list.html'

class ReviewCreate(CreateView):
    form_class = ReviewCreateForm
    template_name = 'ReviewsApp/review_form.html'
    def form_valid(self, form):
        form.instance.user_from = self.request.user
        return super().form_valid(form)