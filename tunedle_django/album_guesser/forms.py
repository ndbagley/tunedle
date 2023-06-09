from django import forms 


class MakeGuess(forms.Form):
    artist = forms.CharField(max_length=100, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Artist'}))
    album = forms.CharField(max_length=100, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Album'}))

    