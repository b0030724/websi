from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text='Required. 150 characters or fewer.')
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    date_of_birth = forms.DateField(required=False)
    town = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Profile
        fields = ['image', 'date_of_birth', 'town']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user.username = self.cleaned_data['username']
        profile.user.first_name = self.cleaned_data['first_name']
        profile.user.last_name = self.cleaned_data['last_name']
        if commit:
            profile.user.save()
            profile.save()
        return profile


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
