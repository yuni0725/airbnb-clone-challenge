from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweet",
    )

    def __str__(self):
        return f"{self.payload}"

    def count_like(self):
        return self.like.count()


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="like",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="like",
    )

    def __str__(self):
        return f"Like of {self.tweet}"
