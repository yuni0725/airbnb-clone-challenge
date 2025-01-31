from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Tweet


class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"
