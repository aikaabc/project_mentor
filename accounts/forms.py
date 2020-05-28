from django import forms
from django.contrib.auth.models import Student
from .models import Mentor
from allauth.socialaccount.forms import SignupForm

class CustomSignupForm(SignupForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)t Name')
    
    def signup(self, request, user):
        user.first_name = forms.CharField(max_length=30, label='First Name')
        user.last_name = forms.CharField(max_length=30, label='Last Name')
        user.save()
        return user



class LoginForm(forms.Form):
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.') 
        return cd['password2']


class UserEditForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')