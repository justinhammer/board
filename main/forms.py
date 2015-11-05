from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div, ButtonHolder
from crispy_forms.bootstrap import FormActions
from main.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name")


class UserLogin(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['user_bio', 'profile_pic']

        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_action = '/user_detail_view/%s/' % self.instance.pk
            self.helper.layout.append(
                FormActions(
                    self.helper.add_input(Submit('submit', 'Submit', css_class="btn-primary"))
                )
            )

            # self.helper.add_input(Submit('submit', 'Submit'))

            # super(UserEditForm, self).__init__(*args, **kwargs)