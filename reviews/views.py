from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm


# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            request.session['user_name'] = form.cleaned_data['user_name']
            return HttpResponseRedirect('/thank_you')
    else :
        form = ReviewForm()
        
    return render(request, 'reviews/review.html', {'form': form})

def thank_you(request):
    user_name = request.session.get('user_name')
    return render(request, 'reviews/thank_you.html', {'user_name': user_name})