from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializers
from .models import User
from tweets.serializer import TweetSerializer


# Create your views here.
class AllUser(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializers(users, many=True)

        return Response(serializers.data)


class DetailUser(APIView):
    def get_object(self, pk):
        all_user = User.objects.get(pk=pk)
        return all_user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)


class UserTweet(APIView):
    def get_object(self, pk):
        user = User.objects.get(pk=pk)
        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = TweetSerializer(user.tweet, many=True)
        return Response(serializer.data)
