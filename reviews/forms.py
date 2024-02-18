from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=100, 
                                error_messages={'required': 'Please enter your name', 'max_length': 'Please enter a shorter name'})
    review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200, error_messages={'required': 'Please enter your feedback'})
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5, error_messages={'required': 'Please enter a rating', 'min_value': 'Please enter a value between 1 and 5', 'max_value': 'Please enter a value between 1 and 5'})