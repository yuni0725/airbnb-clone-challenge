from users.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .models import Tweet
from .serializer import TweetSerializer


class AllTweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        return Response(TweetSerializer(tweets, many=True).data)


class DetailTweet(APIView):
    def get_object(self, user_id):
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound

        return Tweet.objects.filter(user=user_id)

    def get(self, request, user_id):
        user_tweet = self.get_object(user_id)
        return Response(TweetSerializer(user_tweet, many=True).data)
