from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
    ParseError,
    NotAuthenticated,
)
from rest_framework.views import APIView
from .models import Tweet
from .serializer import DetailTweetSerializer, TweetSerializer


class AllTweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        return Response(TweetSerializer(tweets, many=True).data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = DetailTweetSerializer(data=request.data)
            if serializer.is_valid():
                tweets = serializer.save(user=request.user)
                return Response(TweetSerializer(tweets).data)
            else:
                raise serializer.errors
        else:
            raise PermissionDenied


class DetailTweet(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        return Response(DetailTweetSerializer(tweet).data)

    def put(self, request, pk):
        tweet = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != tweet.user:
            raise PermissionDenied

        serializer = DetailTweetSerializer(tweet, data=request.data, partial=True)
        if serializer.is_valid():
            edited_tweet = serializer.save()

            return Response(DetailTweetSerializer(edited_tweet).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != tweet.user:
            raise PermissionDenied
        tweet.delete()
        return Response(HTTP_204_NO_CONTENT)
