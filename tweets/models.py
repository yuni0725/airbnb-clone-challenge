from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Tweet by {self.user}"


class Like(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE)

    def __str__(self):
        return f"Like of {self.tweet}"
