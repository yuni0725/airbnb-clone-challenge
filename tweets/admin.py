from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "count_like",
        "created_at",
        "updated_at",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "created_at",
        "updated_at",
    )
