from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review


# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # Making a new Review object from the form data
            review = Review(
                user_name=form.cleaned_data['user_name'], 
                review_text=form.cleaned_data['review_text'], 
                rating=form.cleaned_data['rating'])
            
            # Giving the username to the session
            request.session['user_name'] = form.cleaned_data['user_name']
            
            # Saving the review to the database
            review.save()
            return HttpResponseRedirect('/thank_you')
    else :
        form = ReviewForm()
        
    return render(request, 'reviews/review.html', {'form': form})

def thank_you(request):
    user_name = request.session.get('user_name')
    return render(request, 'reviews/thank_you.html', {'user_name': user_name})