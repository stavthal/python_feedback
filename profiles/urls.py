from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="create_profile"),
    path("all", views.ProfileListView.as_view(), name="profile_list")
] 
