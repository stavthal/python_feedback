from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class ReviewView(View):
    def get(self, request):
         form = ReviewForm()
        
         return render(request, 'reviews/review.html', {'form': form})
        
    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # Saving the form to the database
            form.save()
            
            # Giving the username to the session
            request.session['user_name'] = form.cleaned_data['user_name']

            return HttpResponseRedirect('/thank_you')

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