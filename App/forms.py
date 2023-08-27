from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class signUpForm(UserCreationForm):
    email=forms.EmailField(label='Email',widget=forms.TextInput(), required=True)
    first_name=forms.CharField(label='FirstName',widget=forms.TextInput(),max_length=100, required=True)
    last_name= first_name=forms.CharField(label='LastName',widget=forms.TextInput(),max_length=100, required=True)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

class AddForm(forms.ModelForm):
    class Meta:
        model=Record
        exclude=('created_at',)