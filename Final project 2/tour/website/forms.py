from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Vendorf

class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Vendorform(forms.ModelForm):
    class Meta:
        model = Vendorf
        fields = '__all__'