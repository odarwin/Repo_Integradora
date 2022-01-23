"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile
from users.models import UserLogin


class UserLoginForm(forms.Form):
    user = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100)
    class Meta:
        model=UserLogin
        fields=('user', 'password')


class SignupForm(forms.Form):
    """Sign up form."""
    firstName = forms.CharField(max_length=200,widget=forms.TextInput())
    lastName = forms.CharField(max_length=200,widget=forms.TextInput())
    CI=forms.CharField(max_length=10,widget=forms.TextInput()) #cedula

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )



    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        # modeloProfile=Profile.objects.create(firstName=data['firstName'],lastName=data['lastName'],CI=data['CI'])
        user = User.objects.create_user(data['username'],data['email'],data['password'])
        profile = Profile(user=user,firstName=data['firstName'],lastName=data['lastName'],CI=data['CI'])
        profile.save()