from django.contrib.auth.forms import UserCreationForm
from django import forms
from main.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name")
