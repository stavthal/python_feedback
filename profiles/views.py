from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView

from .models import Profile
from .forms import ProfileForm

# Create your views here.


class CreateProfileView(FormView):
    # def get(self, request):
    form_class = ProfileForm
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
    object_name = "form"

    # def post(self, request):
    #     print(request.FILES["profile_pic"])
    #     return HttpResponseRedirect("/profiles")
