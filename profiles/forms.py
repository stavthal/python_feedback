from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "bio": "Biography",
            "email": "Email Address",
            "profile_pic": "Profile Picture"
            
        }
        error_messages = {
            "first_name": {
                "required": "Your name must not be empty",
                "max_length": "Enter a shorter name"
            },
            "last_name": {
                "required": "Your name must not be empty",
                "max_length": "Enter a shorter name"
            },
            "bio": {
                "required": "Your bio must not be empty",
                "max_length": "Enter a shorter bio"
            },
            "email": {
                "required": "Your email must not be empty",
                "invalid": "Enter a valid email"
            },
            "profile_pic": {
                "required": "You must upload a profile picture"
            }
        }