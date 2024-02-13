from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class inscriptionform(UserCreationForm):
    prenom = forms.CharField(max_length=50)
    nom = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    
    class meta:
        model = User
        fields = ("username", "password1", "password2", "email", "nom","prenom")
        
    def save(self,commit=True):
        user = super(inscriptionform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.nom = self.cleaned_data['nom']
        user.prenom = self.cleaned_data['prenom']
        
        if commit:
            user.save()
        return user