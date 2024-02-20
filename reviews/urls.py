from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank_you', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews', views.ReviewsListView.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.SingleReviewView.as_view(), name='single_review')

]