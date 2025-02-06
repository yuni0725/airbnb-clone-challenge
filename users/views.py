from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializers
from .models import User
from tweets.serializer import TweetSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import status


# Create your views here.
class AllUser(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializers(users, many=True)

        return Response(serializers.data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise exceptions.ParseError
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)  # hashing the password
            user.save()
            serializer = UserSerializers(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


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


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise exceptions.ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error": "wrong pw"})


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise exceptions.ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
