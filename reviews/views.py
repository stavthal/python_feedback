from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

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
    
class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context
    
class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs['id']
        selected_review = Review.objects.get(pk=review_id) # Select a review based on the review_id
        context['review'] = selected_review
        
        print(context)
        return context # returns the context containing the selected review