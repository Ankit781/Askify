class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = EndUser.objects.get(email=email)
        except EndUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return EndUser.objects.get(pk=user_id)
        except EndUser.DoesNotExist:
            return None
