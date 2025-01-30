from django.urls import path
from . import views


urlpatterns = [
    path("api/v1/tweets", views.see_all_tweet),
    path("api/v1/users/<int:user_id>/tweets", views.user_tweet),
]
