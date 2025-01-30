from users.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Tweet
from .serializer import TweetSerializer


@api_view(["GET"])
def see_all_tweet(request):
    tweets = Tweet.objects.all()
    return Response(TweetSerializer(tweets, many=True).data)


@api_view(["GET"])
def user_tweet(request, user_id):
    try:
        User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise NotFound

    user_tweet = Tweet.objects.filter(user=user_id)
    return Response(TweetSerializer(user_tweet, many=True).data)
