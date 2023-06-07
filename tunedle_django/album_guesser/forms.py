from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class MakeGuess(forms.Form):
    guess = forms.CharField(max_length=100, label='')