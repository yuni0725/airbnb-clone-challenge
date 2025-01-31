from django.urls import path
from . import views


urlpatterns = [
    path("api/v1/tweets", views.AllTweets.as_view()),
    path("api/v1/users/<int:user_id>/tweets", views.DetailTweet.as_view()),
]
