from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from learning_app.models import UserModel


class Authentication(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        user_model = UserModel()
        try:
            user = UserModel.objects.all().get(email=username, password=password)
            print(user)
        except user_model.DoesNotExist:
            return None
        else:
            return user
        return None
