from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Tweet
from users.serializer import TinyUserSerializers


class TweetSerializer(ModelSerializer):
    user = TinyUserSerializers(read_only=True)

    class Meta:
        model = Tweet
        fields = "id", "payload", "user"


class DetailTweetSerializer(ModelSerializer):
    user = TinyUserSerializers(read_only=True)

    like = serializers.SerializerMethodField()

    def get_like(self, tweet):
        return tweet.count_like()

    class Meta:
        model = Tweet
        fields = ("id", "user", "like", "payload")
