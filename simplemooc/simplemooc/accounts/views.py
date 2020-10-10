from django.conf import settings
from django.shortcuts import render, redirect

from .form import RegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    template_name = 'accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)
