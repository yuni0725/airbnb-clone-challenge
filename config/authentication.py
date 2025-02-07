from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from users.models import User


class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("X-USERNAME")

        if not username:
            return None

        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            return exceptions.AuthenticationFailed(f"No username : {username}")
