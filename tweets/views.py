from django.shortcuts import render
from .models import Tweet


def see_all_tweet(request):
    tweets = Tweet.objects.all()
    return render(request, "all_room.html", {"tweets": tweets})
