from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .form import RegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    template_name = 'accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)
