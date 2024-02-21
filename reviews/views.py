from typing import Any
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Gets the context from the parent class
        loaded_review = self.object # Gets the review that was loaded by the DetailView
        request = self.request # Gets the request so we can use the session
        favorite_id = request.session.get("favorite_review_id") # Gets the ID of the review stored in the session
        context["is_favorite"] = favorite_id == str(loaded_review.id) # Adds a new key to the context dictionary
        return context # Returns the context dictionary

class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST['review_id'] # Gets the ID of the review from the form
        request.session['favorite_review_id'] = review_id # Saves the review ID in the session
        return HttpResponseRedirect('/reviews/' + review_id) # Redirects to the review page