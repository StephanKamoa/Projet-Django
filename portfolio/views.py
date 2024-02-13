from imaplib import _Authenticator
from django.shortcuts import render, redirect
from .forms import inscriptionform
from django.views.generic import TemplateView
from .models import *
# Create your views here.



class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['competences'] = Competence.objects.all()
        context['projets'] =  Projet.objects.all()
        context['clients'] =  Client.objects.all()

        
        return context

def ConnexionView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = _Authenticator( username=username, password=password)
        if user is not None:
            ConnexionView(request, user)
            return render('contactView')
    else:
        return render(request, 'connexion.html')
    
def inscriptionView(request):
    if request.method == 'POST':
        form = inscriptionform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form = form.set_password(form.cleaned_data['password'])
            form.save()
            return redirect('ConnexionView')
    else:
        form = inscriptionform()
    return render(request, 'inscription.html',{'form':form})


    
def contactView(request):
    return render(request, 'contact.html')