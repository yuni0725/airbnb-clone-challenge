from django.contrib import admin
from .models import Tweet, Like


class ElonFilter(admin.SimpleListFilter):
    title = "Elon Musk"

    parameter_name = "search"

    def lookups(self, request, model_admin):
        return [
            ("musk", "Elon Musk Contain?"),
        ]

    def queryset(self, request, queryset):
        search = self.value()
        if search:
            return queryset.filter(
                payload__icontains="Elon Musk",
            )


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "count_like",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        ElonFilter,
    )

    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = ("user__username",)

    list_filter = ("created_at",)
