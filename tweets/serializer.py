from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    payload = serializers.CharField(max_length=180)
    user = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
