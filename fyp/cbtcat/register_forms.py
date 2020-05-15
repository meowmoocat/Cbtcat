from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    consent = forms.BooleanField(label='consent')

    def check_password_match(self, password1, password2):
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'consent']
