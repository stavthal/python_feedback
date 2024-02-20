from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import Profile

def store_file(file):
    # Consider enhancing this function to handle file storage more safely and efficiently
    with open("temp/profile_pic.jpg", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = Profile
    fields = "__all__"
    success_url = "/profiles"
    

class ProfileListView(ListView):
    template_name = "profiles/user_profiles.html"
    model = Profile
    context_object_name = "profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self,request): 
#         store_file(request.FILES["profile_pic"]) # stores the file in the temp folder
#         submitted_form = ProfileForm(request.POST, request.FILES)
        
#         if submitted_form.is_valid():
#             profile = Profile(profile_pic=request.FILES["profile_pic"],
#                               first_name=submitted_form.cleaned_data["first_name"],
#                               last_name=submitted_form.cleaned_data["last_name"],
#                               bio=submitted_form.cleaned_data["bio"],
#                               email=submitted_form.cleaned_data["email"])
#             profile.save()
#             return HttpResponseRedirect(reverse_lazy("create_profile"))
        
#         return HttpResponseRedirect(reverse_lazy("create_profile"))
