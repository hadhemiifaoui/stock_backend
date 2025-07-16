# core/forms.py

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models.user import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_name', 'role', 'profile_pic', 'is_staff', 'is_active')

    def clean_password2(self):
        pw1 = self.cleaned_data.get("password1")
        pw2 = self.cleaned_data.get("password2")
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("Passwords don't match")
        return pw2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('user_name', 'password', 'role', 'profile_pic', 'is_active', 'is_staff', 'groups', 'user_permissions')

    def clean_password(self):
        return self.initial["password"]
