from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class ReviewView(FormView):
    
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank_you"

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.session.get('user_name')
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reviews'] = Review.objects.all()
    #     return context
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=4)
        return data
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"