from django.urls import path
from . import views


urlpatterns = [
    path("", views.AllUser.as_view()),
    path("<int:pk>/", views.DetailUser.as_view()),
    path("<int:pk>/tweets", views.UserTweet.as_view()),
]
